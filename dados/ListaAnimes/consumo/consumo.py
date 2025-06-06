
"""
Nesse aquivo vc encontrará os recursos para consumir sua base se dados.
Esse projeto vai ser focado em funcionamento, portando nao teremos classes ou enteidades.
"""	
import pandas as pd
import json
from pymongo import MongoClient

def base_to_dataframe(path: str) -> pd.DataFrame:
    """
    Lê um arquivo JSON e converte para um DataFrame do Pandas.
    
    Args:
        path (str): Caminho do arquivo JSON.
        
    Returns:
        pd.DataFrame: DataFrame contendo os dados do JSON.
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return pd.DataFrame(data)

def dataframe_to_mongodb(df: pd.DataFrame, collection_name: str, mongo_uri: str):
    """
    Converte um DataFrame do Pandas para uma coleção MongoDB.
    
    Args:
        df (pd.DataFrame): DataFrame a ser convertido.
        collection_name (str): Nome da coleção no MongoDB.
        mongo_uri (str): URI de conexão com o MongoDB.
    """
    client = MongoClient(mongo_uri)
    db = client.get_default_database()
    collection = db[collection_name]
    
    # Limpa a coleção antes de inserir novos dados
    collection.delete_many({})
    
    # Insere os dados do DataFrame na coleção
    collection.insert_many(df.to_dict('records'))


#########################################################################################

def clean_dataframe_column_nulls(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Limpa os valores nulos de uma coluna específica de um DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame a ser limpo.
        column_name (str): Nome da coluna a ser limpa.
        
    Returns:
        pd.DataFrame: DataFrame com valores nulos removidos da coluna especificada.
    """
    df[column_name] = df[column_name].dropna()
    return df

def clean_dataframe_column_duplicates(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Remove duplicatas de uma coluna específica de um DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame a ser limpo.
        column_name (str): Nome da coluna a ser limpa.
        
    Returns:
        pd.DataFrame: DataFrame com duplicatas removidas da coluna especificada.
    """
    df[column_name] = df[column_name].drop_duplicates()
    return df

def clean_dataframe_column_empty(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Remove valores vazios de uma coluna específica de um DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame a ser limpo.
        column_name (str): Nome da coluna a ser limpa.
        
    Returns:
        pd.DataFrame: DataFrame com valores vazios removidos da coluna especificada.
    """
    df[column_name] = df[column_name].replace('', pd.NA).dropna()
    return df