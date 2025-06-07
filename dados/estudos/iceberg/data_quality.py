# Exemplo de como emitir uma métrica personalizada para o CloudWatch (dentro do seu Glue Job de DQ)
import boto3
import json

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1') # ou sua região

def put_cloudwatch_metric(metric_name, value, dimensions, namespace="SeuProjeto/DataQuality"):
    try:
        cloudwatch.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': dimensions,
                    'Value': value,
                    'Unit': 'Count' # Ou 'Percent', 'Seconds', etc.
                },
            ]
        )
        print(f"Métrica '{metric_name}' enviada para CloudWatch: {value} com dimensões {dimensions}")
    except Exception as e:
        print(f"Erro ao enviar métrica para CloudWatch: {e}")

# Exemplo de uso no seu job de DQ após calcular os resultados:
# put_cloudwatch_metric(
#     metric_name="RegistrosComErro",
#     value=invalid_records_count,
#     dimensions=[
#         {'Name': 'Processo', 'Value': 'processo_posvenda'},
#         {'Name': 'Area', 'Value': 'Comercial'},
#         {'Name': 'TipoErro', 'Value': 'ValorInvalido'},
#     ]
# )