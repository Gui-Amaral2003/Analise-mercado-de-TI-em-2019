import data_fetch as df
import cleaning_real_state as clean
import pyspark.sql.functions as F
from pyspark.ml.feature import StringIndexer, OneHotEncoder, StandardScaler, VectorAssembler

def sqft_to_m2(df):
    df = df.withColumn('m2', F.round(F.col('sqft') / 10.764, 2))
    
    return df

def col_ratio(df, col1, col2):
    df = df.withColumn(f'{col1}_to_{col2}', F.round(F.col(col1) / F.when(F.col(col2) != 0, F.col(col2)).otherwise(1), 2))
    
    return df

def one_hot(df, col):
    indexer = StringIndexer(inputCol=col, outputCol=f'{col}_idx')
    encoder = OneHotEncoder(inputCol=indexer.getOutputCol(), outputCol=f'{col}_vec')
    
    return indexer, encoder

def normalizer(df):
    numerical_cols = ['year_built', 'beds', 'baths', 'garage', 'sqft', 'stories', 'm2', 'baths_to_m2', 'baths_to_beds', 'baths_to_stories', 'beds_to_m2', 'beds_to_stories']

    ##Montando o vetor de features numericas
    assembler = VectorAssembler(inputCols=numerical_cols, outputCol="features_vector")
    df_assembled = assembler.transform(df)

    ##Aplicando o StandardScaler
    scaler = StandardScaler(inputCol="features_vector", outputCol="features_scaled", withMean=True, withStd=True)
    scaler_model = scaler.fit(df_assembled)
    df_scaled = scaler_model.transform(df_assembled)
    
    return df_scaled


def prepare_df(real_state):
    ##Limpando o df
    real_state = clean.removing_col(real_state, ['text', 'baths_half', 'baths_full', 'lot_sqft', 'soldOn', 'lastSoldPrice', 'status'])
    real_state = clean.fillna(real_state, ['year_built', 'beds', 'baths', 'sqft', 'stories', 'listPrice', 'garage'])
    real_state = clean.removing_lines(real_state)
    
    ##Criando as features
    real_state = sqft_to_m2(real_state)
    
    real_state = col_ratio(real_state, 'baths', 'm2')
    real_state = col_ratio(real_state, 'baths', 'beds')
    real_state = col_ratio(real_state, 'baths', 'stories')
    real_state = col_ratio(real_state, 'beds', 'm2')
    real_state = col_ratio(real_state, 'beds', 'stories')
    real_state = col_ratio(real_state, 'garage', 'm2')
    real_state = normalizer(real_state)
    
    ##Removendo colunas redundantes
    real_state = clean.removing_col(real_state,  ['year_built', 'beds', 'baths', 'garage', 'sqft', 'stories', 'm2', 'baths_to_m2', 'baths_to_beds', 'baths_to_stories', 'beds_to_m2', 'beds_to_stories', 'features_vector'])
    
    return real_state
    
    