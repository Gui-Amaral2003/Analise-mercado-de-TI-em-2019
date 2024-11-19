import data_fetch as fd
import pyspark.sql.functions as F

real_state = fd.fetch_data()

def removing_col(df, colNames: list):
    return df.drop(*colNames)

def medianas(df, cols):
    medias = dict()
    
    for c in cols:
        valor = df.approxQuantile(c, [0.5], 0.1)[0]
        medias[c] = valor
    return medias

def fillna(df, cols):
    m = medianas(df, cols)
    df = df.fillna(m)
    
    return df

def removing_lines(df):
    df = df.filter(df['stories'] != 119)
    df = df.filter(df['garage'] != 400)
    return df