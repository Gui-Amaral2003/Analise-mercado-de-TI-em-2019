import pandas as pd


def porcentagem_valor(df: pd.DataFrame, coluna = "Churn", valor = 1):
    numerador = df[df[coluna] == valor].shape[0]
    denominador = df.shape[0]
    
    return round(numerador/denominador, 2) * 100

def separar_df(df: pd.DataFrame, coluna, valor):
    df_separado = df[df[coluna] == valor]
    
    return df_separado

def valor_mais_comum(df: pd.DataFrame, coluna):
    contagem = df[coluna].value_counts()
    
    return contagem.index[0]

def somar_coluna(df: pd.DataFrame, coluna):
    return df[coluna].sum()

def correlacao(df: pd.DataFrame, coluna):
    corr = df.corr()[coluna].abs()
    print(corr.sort_values())
    