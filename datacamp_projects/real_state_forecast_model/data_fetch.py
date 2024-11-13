import pandas as pd
from pyspark.sql import SparkSession


def fetch_data(url = "https://drive.google.com/file/d/1MzVbSI-SOwkjk7tkguzf7jhSKZBcQ1KS/view?usp=sharing", type='pyspark'):
    
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    df = pd.read_csv(url)
    
    if(type == 'pyspark'):
        # Inicializando a sessão Spark
        spark = SparkSession.builder.appName("FetchData").getOrCreate()
        df1 = spark.createDataFrame(df)
        return df1
    else:
        return df