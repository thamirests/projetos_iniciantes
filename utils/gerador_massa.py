# -*- coding: utf-8 -*-
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import os
from faker import Faker
from datetime import datetime, timedelta
import random
import sys

# --- Configurações da Geração de Dados ---
NUM_REGISTROS = 2000 # Total de registros a serem gerados
NUM_CLIENTES = 2
NUM_PROCESSOS_FIXOS = 5 # Venda, PosVenda, Faturamento, Cobranca, Suporte
DIAS_HISTORICO = 30 # Gerar dados para os últimos 30 dias
OUTPUT_DIR = "local_data_origin" # Diretório onde os arquivos Parquet serão salvos

# Inicializa o Faker para dados randômicos
fake = Faker('pt_BR') # Usar localidade brasileira para nomes/endereços

# Lista de processos e áreas correspondentes
PROCESSOS_AREAS = {
    "processo_venda": "Comercial",
    "processo_posvenda": "Comercial",
    "processo_faturamento": "Financeiro",
    "processo_cobranca": "Financeiro",
    "processo_suporte": "Atendimento"
}

# --- Função para Gerar Dados de um Registro ---
def generate_record(client_id, process_name, date_obj):
    """Gera um único registro com dados randômicos."""
    area = PROCESSOS_AREAS.get(process_name, "Desconhecido")
    
    return {
        "registro_id": fake.uuid4(),
        "client_id": client_id,
        "area": area, # Adicionando a coluna 'area' para compatibilidade com o Glue Job Iceberg
        "processo_nome": process_name,
        "data_carga": date_obj, # Timestamp
        "valor_transacao": round(random.uniform(10.0, 1000.0), 2),
        "outra_coluna_texto": fake.sentence(),
        "outra_coluna_inteiro": random.randint(1, 1000),
        # Colunas de partição para a tabela de origem (serão extraídas do timestamp)
        "ano": str(date_obj.year),
        "mes": str(date_obj.month).zfill(2), # Adiciona zero à esquerda se for menor que 10
        "dia": str(date_obj.day).zfill(2)   # Adiciona zero à esquerda se for menor que 10
    }

# --- Geração dos Dados ---
print(f"Gerando {NUM_REGISTROS} registros para {NUM_CLIENTES} clientes e {NUM_PROCESSOS_FIXOS} processos fixos.")
data = []
client_ids = [f"cliente_{i+1}" for i in range(NUM_CLIENTES)]
process_names = list(PROCESSOS_AREAS.keys())

for _ in range(NUM_REGISTROS):
    client_id = random.choice(client_ids)
    process_name = random.choice(process_names)
    
    # Gera uma data randômica dentro do histórico definido
    random_days_ago = random.randint(0, DIAS_HISTORICO - 1)
    data_carga_obj = datetime.now() - timedelta(days=random_days_ago)
    data_carga_obj = data_carga_obj.replace(
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59),
        microsecond=0
    )
    
    data.append(generate_record(client_id, process_name, data_carga_obj))

df = pd.DataFrame(data)

# Garante que 'data_carga' é do tipo datetime
df['data_carga'] = pd.to_datetime(df['data_carga'])

print(f"DataFrame Pandas criado com {len(df)} registros.")
print("Amostra do DataFrame:")
print(df.head())
print("\nTipos de dados inferidos:")
print(df.dtypes)

# --- Escrita no Formato Parquet com Particionamento ---
print(f"\nEscrevendo dados no formato Parquet com particionamento em: {OUTPUT_DIR}")

# Define as colunas de partição para a escrita do Parquet
PARTITION_COLS = ['processo_nome', 'ano', 'mes', 'dia']

# Cria o diretório de saída se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    # Usando pyarrow para escrever o DataFrame Pandas como Parquet particionado
    # Isso cria uma estrutura de pastas como:
    # local_data_origin/processo_nome=processo_venda/ano=2025/mes=06/dia=07/part-00000.parquet
    table = pa.Table.from_pandas(df)
    pq.write_to_dataset(
        table,
        root_path=OUTPUT_DIR,
        partition_cols=PARTITION_COLS,
        basename_template="part-{i}.parquet" # Nomeia os arquivos parquet
    )
    print(f"\nArquivos Parquet gerados com sucesso em '{OUTPUT_DIR}' com a seguinte estrutura de partição:")
    print(f"  Root: {OUTPUT_DIR}/")
    print(f"  Partições: /{'/'.join(PARTITION_COLS)}/")
    
    # Verifica alguns arquivos gerados
    print("\nVerificando alguns diretórios de partição criados:")
    # Apenas percorre alguns níveis para não inundar o console
    walk_count = 0
    for root, dirs, files in os.walk(OUTPUT_DIR):
        if files and any(f.endswith('.parquet') for f in files):
            print(f"- {root}")
            if len(files) > 0:
                print(f"  - {files[0]} (e outros {len(files)-1})")
            walk_count += 1
            if walk_count > 5: # Limita a saída para não poluir muito o console
                break
        if walk_count > 5:
            break


except Exception as e:
    print(f"ERRO ao escrever arquivos Parquet: {e}")
    sys.exit(1)

print("\nProcesso de geração de dados concluído.")
