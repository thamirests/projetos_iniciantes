# -*- coding: utf-8 -*-
import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, to_date, date_format
from datetime import datetime, timedelta

# --- 1. Definição das Funções Auxiliares ---

def create_dynamic_frame_origin(
    glue_context: GlueContext,
    source_database: str,
    source_table_name: str,
    push_down_predicate: str = None
):
    """
    Cria um DynamicFrame a partir do AWS Glue Data Catalog, com suporte a pushdown de prediado.

    Args:
        glue_context (GlueContext): O objeto GlueContext.
        source_database (str): Nome do banco de dados no Data Catalog.
        source_table_name (str): Nome da tabela no Data Catalog.
        push_down_predicate (str, optional): Predicado para filtrar partições na leitura. Default é None.

    Returns:
        DynamicFrame: O DynamicFrame lido.

    Raises:
        Exception: Se ocorrer um erro durante a leitura da tabela.
    """
    print(f"Iniciando leitura da tabela de origem: {source_table_name} no DB: {source_database}")
    if push_down_predicate:
        print(f"Aplicando filtro de partição: {push_down_predicate}")

    try:
        dynamic_frame = glue_context.create_dynamic_frame.from_catalog(
            database=source_database,
            table_name=source_table_name,
            push_down_predicate=push_down_predicate,
            transformation_ctx="source_data_read"
        )
        print(f"Leitura da tabela de origem concluída. Esquema do DynamicFrame:\n{dynamic_frame.printSchema()}")
        return dynamic_frame
    except Exception as e:
        error_message = f"ERRO ao criar DynamicFrame da tabela de origem '{source_table_name}': {e}"
        print(error_message)
        raise Exception(error_message) # Re-levanta a exceção para que o job falhe

def perform_basic_data_quality_checks(df: SparkSession.DataFrame, job_name: str) -> SparkSession.DataFrame:
    """
    Realiza verificações básicas de Data Quality no DataFrame.

    Args:
        df (SparkSession.DataFrame): O DataFrame a ser validado.
        job_name (str): Nome do job para logs.

    Returns:
        SparkSession.DataFrame: O DataFrame após a aplicação das regras de DQ.

    Raises:
        ValueError: Se regras críticas de DQ forem violadas.
    """
    print(f"Iniciando verificações básicas de Data Quality para o job: {job_name}")

    initial_count = df.count()
    print(f"DQ: Contagem inicial de registros: {initial_count}")

    # Regra 1: Remover registros onde client_id ou registro_id são nulos
    # Definir colunas críticas como not null
    critical_not_null_cols = ["client_id", "registro_id"]
    df_cleaned_nulls = df.dropna(subset=critical_not_null_cols)
    dropped_null_count = initial_count - df_cleaned_nulls.count()
    if dropped_null_count > 0:
        print(f"DQ: ATENÇÃO! {dropped_null_count} registros removidos devido a valores nulos em colunas críticas ({', '.join(critical_not_null_cols)}).")
        # Se for crítico, você pode levantar um erro ou registrar esses IDs em algum lugar
        # Para fins de demonstração, estamos apenas logando e removendo.
        # raise ValueError(f"Registros com valores nulos críticos encontrados. Job falhou.")
    else:
        print("DQ: Nenhuma linha com valores nulos críticos encontrada.")
    df = df_cleaned_nulls


    # Regra 2: Remover duplicatas em chaves primárias (se a combinação for única)
    # Supondo que a combinação de client_id e registro_id deve ser única
    primary_key_cols = ["client_id", "registro_id"]
    df_deduplicated = df.dropDuplicates(subset=primary_key_cols)
    dropped_duplicates_count = df.count() - df_deduplicated.count()
    if dropped_duplicates_count > 0:
        print(f"DQ: ATENÇÃO! {dropped_duplicates_count} registros duplicados removidos com base em ({', '.join(primary_key_cols)}).")
    else:
        print("DQ: Nenhuma duplicata encontrada para as chaves primárias.")
    df = df_deduplicated

    # Regra 3: Validação de range para valor_transacao (ex: deve ser positivo)
    # Assumindo que 'valor_transacao' é uma coluna numérica
    if "valor_transacao" in df.columns:
        invalid_transactions = df.filter(col("valor_transacao") <= 0).count()
        if invalid_transactions > 0:
            print(f"DQ: ALERTA! {invalid_transactions} registros com 'valor_transacao' inválido (<= 0).")
            # Para fins de demonstração, estamos apenas logando. Você pode optar por filtrar esses registros.
            # df = df.filter(col("valor_transacao") > 0)
            # print("DQ: Registros com 'valor_transacao' inválido foram filtrados.")
        else:
            print("DQ: Todos os 'valor_transacao' são válidos (> 0).")
    else:
        print("DQ: Coluna 'valor_transacao' não encontrada. Pulando validação de range.")
    
    # Adicione outras regras de DQ básicas conforme necessário
    # Ex: Validação de formato de data se for string e precisar ser timestamp
    # df = df.withColumn("data_carga_validada", to_timestamp(col("data_carga"), "yyyy-MM-dd HH:mm:ss"))
    # df = df.dropna(subset=["data_carga_validada"])

    final_count = df.count()
    print(f"DQ: Contagem final de registros após DQ básica: {final_count}")
    if final_count == 0 and initial_count > 0:
        print("DQ: ATENÇÃO! Todos os registros foram filtrados/removidos por regras de DQ. DataFrame vazio.")
        # Considere levantar um erro aqui se um DataFrame vazio for um problema após DQ

    print("Verificações básicas de Data Quality concluídas.")
    return df

def write_iceberg_table(
    spark_session: SparkSession, # Passa a sessão Spark para executar SQL DELETE
    df: SparkSession.DataFrame,
    iceberg_table_name: str,
    output_s3_path: str,
    partition_keys: list,
    reprocess_params: dict = None # Dicionário com os parâmetros de reprocessamento para modo 'daily'
):
    """
    Escreve um Spark DataFrame em uma tabela Apache Iceberg particionada no S3.
    Inclui lógica de auditoria para contar registros existentes antes do overwrite.
    Se o DataFrame for vazio para uma partição específica no modo 'daily', executa um DELETE.

    Args:
        spark_session (SparkSession): A sessão Spark.
        df (SparkSession.DataFrame): O DataFrame a ser escrito.
        iceberg_table_name (str): Nome completo da tabela Iceberg no Glue Data Catalog (ex: db.table_name).
        output_s3_path (str): Caminho raiz do S3 onde a tabela Iceberg será armazenada.
        partition_keys (list): Lista de colunas ou transformações de particionamento (ex: [col("client_id"), "months(data_carga)"]).
        reprocess_params (dict, optional): Dicionário com os parâmetros de reprocessamento para o modo 'daily'. Default é None.

    Raises:
        Exception: Se ocorrer um erro durante a escrita ou deleção na tabela Iceberg.
    """
    print(f"Iniciando operação na tabela Iceberg: {iceberg_table_name}")
    new_records_count = df.count()
    print(f"Número de registros no DataFrame de entrada (novos/reprocessados): {new_records_count}")

    # Construir a cláusula WHERE para o DELETE e a verificação de COUNT(*)
    # Essa parte só é relevante para o modo 'daily' quando reprocess_params é fornecido.
    current_partition_filter_sql = ""
    if reprocess_params:
        # Assumindo que 'area' e 'data_carga' são colunas no seu DataFrame/tabela Iceberg
        reprocess_date_str = f"{reprocess_params['REPROCESS_YEAR']}-{reprocess_params['REPROCESS_MONTH']}-{reprocess_params['REPROCESS_DAY']}"
        current_partition_filter_sql = f"""
            WHERE area = '{reprocess_params['REPROCESS_AREA']}'
              AND processo_nome = '{reprocess_params['REPROCESS_PROCESS']}'
              AND to_date(data_carga) = '{reprocess_date_str}'
        """
        print(f"Filtro de partição para operação: {current_partition_filter_sql}")

    try:
        if new_records_count > 0:
            # Contar registros existentes ANTES do overwrite, apenas se for uma partição específica
            existing_records_count = 0
            if current_partition_filter_sql:
                check_existing_sql = f"SELECT count(*) FROM glue_catalog.{iceberg_table_name} {current_partition_filter_sql}"
                print(f"Verificando registros existentes na partição com: {check_existing_sql}")
                existing_records_count = spark_session.sql(check_existing_sql).collect()[0][0]
                print(f"Encontrados {existing_records_count} registros existentes para a partição antes da escrita.")

            print("DataFrame não vazio. Realizando overwrite de partições...")
            df.writeTo(iceberg_table_name) \
                .option("path", output_s3_path) \
                .partitionedBy(*partition_keys) \
                .overwritePartitions() \
                .save()
            print("Escrita na tabela Iceberg concluída com sucesso.")
            
            # Log de auditoria
            if current_partition_filter_sql:
                print(f"MÉTRICA_AUDITORIA: {new_records_count} registros na nova partição. {existing_records_count} registros foram sobrescritos.")
            else: # Modo 'full' ou sem filtro específico
                print(f"MÉTRICA_AUDITORIA: {new_records_count} registros escritos (modo completo ou nova partição).")

        else: # df.count() == 0
            print("DataFrame de entrada está vazio.")
            if current_partition_filter_sql: # Apenas tentar apagar se estiver em modo 'daily' e com filtro de partição
                existing_records_count = 0
                check_existing_sql = f"SELECT count(*) FROM glue_catalog.{iceberg_table_name} {current_partition_filter_sql}"
                print(f"Verificando existência de dados para deleção com: {check_existing_sql}")
                existing_records_count = spark_session.sql(check_existing_sql).collect()[0][0]

                if existing_records_count > 0:
                    print(f"Encontrados {existing_records_count} registros existentes para a partição. Executando DELETE...")
                    delete_sql = f"DELETE FROM glue_catalog.{iceberg_table_name} {current_partition_filter_sql}"
                    print(f"Comando DELETE: {delete_sql}")
                    spark_session.sql(delete_sql)
                    print("Deleção da partição concluída com sucesso.")
                    # Log de auditoria
                    print(f"MÉTRICA_AUDITORIA: 0 registros na nova partição. {existing_records_count} registros foram DELETADOS.")
                else:
                    print("Nenhum registro encontrado para a partição. Nenhuma ação de deleção necessária.")
            else:
                print("Modo 'full' ou sem parâmetros de reprocessamento. Nenhuma deleção de partição vazia é aplicada.")

    except Exception as e:
        error_message = f"ERRO ao operar na tabela Iceberg '{iceberg_table_name}': {e}"
        print(error_message)
        raise Exception(error_message) # Re-levanta a exceção para que o job falhe

# --- 2. Inicialização do Job e Obtenção de Variáveis ---

# @params: [JOB_NAME, S3_TEMP_DIR, TIPO_EXECUCAO, REPROCESS_AREA, REPROCESS_PROCESS, REPROCESS_YEAR, REPROCESS_MONTH, REPROCESS_DAY]
# TIPO_EXECUCAO é 'full' ou 'daily'.
# Os parâmetros REPROCESS_* são opcionais e só devem ser passados se TIPO_EXECUCAO for 'daily'.
try:
    args = getResolvedOptions(sys.argv, [
        'JOB_NAME',
        'S3_TEMP_DIR',
        'TIPO_EXECUCAO',
        'REPROCESS_AREA',
        'REPROCESS_PROCESS',
        'REPROCESS_YEAR',
        'REPROCESS_MONTH',
        'REPROCESS_DAY'
    ])
except Exception as e:
    error_message = f"ERRO ao obter parâmetros do job: {e}. Verifique se todos os parâmetros esperados estão configurados."
    print(error_message)
    sys.exit(1) # Sai do job com erro

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

try:
    job.init(args['JOB_NAME'], args)
except Exception as e:
    error_message = f"ERRO ao inicializar o job do Glue: {e}"
    print(error_message)
    sys.exit(1)

# --- Configurações Iceberg para a Spark Session ---
try:
    spark.conf.set("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")
    spark.conf.set("spark.sql.catalog.glue_catalog.warehouse", args['S3_TEMP_DIR'])
    spark.conf.set("spark.sql.catalog.glue_catalog.type", "hive") # Usar HiveMetastore (Glue Data Catalog)
    spark.conf.set("spark.sql.defaultCatalog", "glue_catalog") # Definir como catálogo padrão
    print("Configurações Iceberg para a Spark Session aplicadas com sucesso.")
except Exception as e:
    error_message = f"ERRO ao configurar a Spark Session para Iceberg: {e}"
    print(error_message)
    job.commit()
    sys.exit(1)

# --- Constantes de Configuração ---
SOURCE_DATABASE = "sua_origem_database" # Ex: "raw_data_db"
SOURCE_TABLE_NAME = "tabela_unica_clientes" # Ex: "tabela_unica_clientes"

# Caminho no S3 onde a tabela Iceberg será armazenada
OUTPUT_ICEBERG_TABLE_PATH = "s3://seu-bucket-de-dados-processados/data_lake/clientes_separados/" # Ex: "s3://my-data-lake-prod/data_lake/clientes_separados/"
# Nome da tabela Iceberg no Glue Data Catalog
ICEBERG_TABLE_NAME = "processed_data_db.tb_processo_cliente" # Ex: "processed_data_db.tb_clientes_detalhes"

# Chaves de particionamento da tabela Iceberg de destino (lógica)
# Ajuste conforme as colunas reais do seu DataFrame e suas transformações de particionamento.
ICEBERG_PARTITION_KEYS = [
    col("client_id"),
    col("area"),
    col("processo_nome"),
    "months(data_carga)" # Supondo que 'data_carga' é um campo timestamp
]

# Dicionário para armazenar os parâmetros de reprocessamento
reprocess_params = {}

# --- 3. Lógica Principal do Job ---
try:
    print(f"Tipo de execução: {args['TIPO_EXECUCAO']}")

    dynamic_frame_origin = None
    if args['TIPO_EXECUCAO'].lower() == 'full':
        dynamic_frame_origin = create_dynamic_frame_origin(
            glue_context=glueContext,
            source_database=SOURCE_DATABASE,
            source_table_name=SOURCE_TABLE_NAME
        )
    elif args['TIPO_EXECUCAO'].lower() == 'daily':
        # Validar e coletar parâmetros de reprocessamento
        required_daily_params = ['REPROCESS_AREA', 'REPROCESS_PROCESS', 'REPROCESS_YEAR', 'REPROCESS_MONTH', 'REPROCESS_DAY']
        if not all(arg in args and args[arg] is not None for arg in required_daily_params):
            raise ValueError(f"Para TIPO_EXECUCAO='daily', todos os parâmetros de reprocessamento são necessários: {required_daily_params}")
        
        reprocess_params = {
            'REPROCESS_AREA': args['REPROCESS_AREA'],
            'REPROCESS_PROCESS': args['REPROCESS_PROCESS'],
            'REPROCESS_YEAR': args['REPROCESS_YEAR'],
            'REPROCESS_MONTH': args['REPROCESS_MONTH'],
            'REPROCESS_DAY': args['REPROCESS_DAY']
        }

        # Construindo a cláusula de pushdown de partição para a tabela de origem Parquet
        # Assumimos que 'processo_nome', 'ano', 'mes', 'dia' são chaves de partição da sua tabela de origem.
        push_down_predicate = (
            f"processo_nome='{reprocess_params['REPROCESS_PROCESS']}' and "
            f"ano='{reprocess_params['REPROCESS_YEAR']}' and "
            f"mes='{reprocess_params['REPROCESS_MONTH']}' and "
            f"dia='{reprocess_params['REPROCESS_DAY']}'"
        )
        dynamic_frame_origin = create_dynamic_frame_origin(
            glue_context=glueContext,
            source_database=SOURCE_DATABASE,
            table_name=SOURCE_TABLE_NAME,
            push_down_predicate=push_down_predicate
        )
    else:
        raise ValueError("Parâmetro TIPO_EXECUCAO inválido. Use 'full' ou 'daily'.")

    # Converta para Spark DataFrame
    df_processed = dynamic_frame_origin.toDF()
    print(f"Número de registros no DataFrame para escrita (após leitura filtrada): {df_processed.count()}")

    # --- Realize qualquer transformação adicional aqui, se necessário ---
    # Garanta que as colunas 'client_id', 'area', 'processo_nome', 'data_carga' existam no df_processed.
    # Exemplo: Se 'area' não estiver na origem e for inferida/derivada, faça-o aqui.
    # df_processed = df_processed.withColumn("area", substring(col("processo_nome"), 1, 5)) # Ex: "Comercial_Venda" -> "Comercial"
    # Adiciona a coluna 'area' ao DataFrame se ela não existir e foi passada como parâmetro no reprocessamento
    if 'area' not in df_processed.columns and 'REPROCESS_AREA' in reprocess_params:
        df_processed = df_processed.withColumn("area", lit(reprocess_params['REPROCESS_AREA']))
        print(f"Coluna 'area' adicionada ao DataFrame com valor: {reprocess_params['REPROCESS_AREA']}")

    # --- Realizar verificações de Data Quality básicas ---
    df_processed_dq = perform_basic_data_quality_checks(df_processed, args['JOB_NAME'])

    # --- Escreva na tabela Iceberg ou execute DELETE ---
    write_iceberg_table(
        spark_session=spark,
        df=df_processed_dq, # Passa o DataFrame JÁ VALIDADO
        iceberg_table_name=ICEBERG_TABLE_NAME,
        output_s3_path=OUTPUT_ICEBERG_TABLE_PATH,
        partition_keys=ICEBERG_PARTITION_KEYS,
        reprocess_params=reprocess_params # Passa os parâmetros para a função de escrita
    )

except Exception as e:
    error_message = f"ERRO FATAL durante a execução do job principal: {e}"
    print(error_message)
    job.commit()
    sys.exit(1)

# --- 4. Commit do Job ---
print("Commiting Glue Job.")
job.commit()
