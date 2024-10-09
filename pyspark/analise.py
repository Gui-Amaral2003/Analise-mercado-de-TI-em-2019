from pandas import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.ml.stat import Correlation

##Criando o ambiente
spark = SparkSession.builder.appName("Análise de dados com PySpark").getOrCreate()


##Carregar o arquivo
df = spark.read.csv('dataframes/customerChurn/Customer Churn.csv', header = True, inferSchema = True)

##Verificando as primeiras linhas
##df.printSchema()

##Calcular a porcentagem de clientes no estado churn
def porcentagem_valor(df: DataFrame, coluna: str = "Churn", valor = 1) -> float:
    numerador = df.filter(df[coluna] == valor).count()
    denominador = df.count()
    
    return round((numerador / denominador) * 100, 2)

##Separar DF
def separar_df(df:DataFrame, coluna: str, valor) -> DataFrame:
    df_separado = df.filter(df[coluna] == valor)
    
    return df_separado

##Calcular o valor mais comum de um DF
def valor_mais_comum(df:DataFrame, coluna: str):
    contagem = df.groupby(coluna).count()
    valor_comum = contagem.orderBy(F.desc('count')).select(coluna).first()[0]
    
    return valor_comum

##Calcular a correlação de uma coluna
from pyspark.ml.feature import VectorAssembler
import numpy as np

def correlacao(df: DataFrame, coluna: str):
    # Selecionar apenas as colunas numéricas
    numeric_cols = [col for col, dtype in df.dtypes if dtype in ('int', 'double')]
    
    # Montar um vetor com as colunas numéricas usando VectorAssembler
    vector_col = "features"
    assembler = VectorAssembler(inputCols=numeric_cols, outputCol=vector_col)
    vector_df = assembler.transform(df).select(vector_col)
    
    # Calcular a matriz de correlação
    corr_matrix = Correlation.corr(vector_df, vector_col).head()[0]
    
    # Converter a matriz de correlação para array
    corr_array = corr_matrix.toArray()
    
    # Obter o índice da coluna desejada
    col_index = numeric_cols.index(coluna)
    
    # Criar uma lista de tuplas com o nome da coluna e a correlação absoluta
    corr_df = [(numeric_cols[i], float(np.abs(corr_array[col_index, i]))) for i in range(len(numeric_cols))]
    
    # Criar um DataFrame PySpark com os resultados
    corr_result_df = spark.createDataFrame(corr_df, ["Coluna", "Correlação"])

    # Ordenar pela correlação
    corr_result_df = corr_result_df.filter(corr_result_df.Coluna != coluna).orderBy(F.col("Correlação"))

    # Exibir o resultado
    corr_result_df.show(truncate=False)

    
df.select(F.stddev('Frequency of Use')).show()