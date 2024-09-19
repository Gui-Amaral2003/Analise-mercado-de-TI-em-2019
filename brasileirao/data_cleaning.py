##TODO: REMOVER COLUNAS DESNECESSARIAS
import pandas as pd
import data_analysis

def remover_coluna(df:pd.DataFrame, cols:list):
    df.drop(cols, axis = 1, inplace = True)
    

def separar_df_por_time(df:pd.DataFrame, time:str):
    df_time = df[(df['mandante'] == time) | (df['visitante'] == time)]
    
    return df_time

def separar_df_por_tecnico(df:pd.DataFrame, tecnico:str):
    df_tec = df[(df['tecnico_mandante'] == tecnico) | (df['tecnico_visitante'] == tecnico)]
    
    return df_tec
    
def limitar_ano(df:pd.DataFrame, ano:int):
    df['data'] = pd.to_datetime(df['data'], format = '%d/%m/%Y')
    
    df_ano = df[df['data'].dt.year == ano]
    
    return df_ano



