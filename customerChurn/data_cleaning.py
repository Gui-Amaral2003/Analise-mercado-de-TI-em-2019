import data_fetch
import data_analysis
import pandas as pd

df = data_fetch.fetch_data()


def remover_duplicatas(df: pd.DataFrame):
    if(df.duplicated().sum() > 0):
        df_clean = df.drop_duplicates()
        
    return df_clean

print(df.dtypes)

def remover_coluna(df: pd.DataFrame, coluna):
    df_rem = df.drop(coluna, axis = 1, inplace = False)
    
    return df_rem