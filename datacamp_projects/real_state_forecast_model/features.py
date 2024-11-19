import data_fetch as df
import cleaning_real_state as clean
import pyspark.sql.functions as F

real_state = df.fetch_data()

def sqft_to_m2(df):
    df = df.withColumn('m2', F.round(F.col('sqft') / 10.764, 2))
    
    return df

def col_ratio(df, col1, col2):
    df = df.withColumn(f'{col1}_to_{col2}', F.round(F.col(col1) / F.when(F.col(col2) != 0, F.col(col2)).otherwise(1), 2))
    
    return df

def binary_cols(df):
    df = df.withColumn('is_large_home', F.when((F.col("beds") > 4) & (F.col("baths") > 3), 1).otherwise(0))
    df = df.withColumn("luxury_indicator", F.when((F.col("listPrice") > 1_000_000) & (F.col("m2") > 300), 1).otherwise(0))
    
    return df


def prepare_df(real_state):
    ##Limpando o df
    real_state = clean.removing_col(real_state, ['text', 'baths_half', 'baths_full', 'lot_sqft', 'soldOn', 'lastSoldPrice', 'status'])
    real_state = clean.fillna(real_state, ['year_built', 'beds', 'baths', 'sqft', 'stories', 'listPrice', 'garage'])
    real_state = clean.removing_lines(real_state)
    
    ##Criando as features
    real_state = sqft_to_m2(real_state)
    
    real_state = binary_cols(real_state)
    
    real_state = col_ratio(real_state, 'baths', 'm2')
    real_state = col_ratio(real_state, 'baths', 'beds')
    real_state = col_ratio(real_state, 'baths', 'stories')
    real_state = col_ratio(real_state, 'beds', 'm2')
    real_state = col_ratio(real_state, 'beds', 'stories')
    real_state = col_ratio(real_state, 'garage', 'm2')
        
    return real_state

##Teste das funções

'''print("Antes de remover colunas:", real_state.count())
real_state = clean.removing_col(real_state, ['text', 'baths_half', 'baths_full', 'lot_sqft', 'soldOn', 'lastSoldPrice', 'status'])
print("Após remover colunas:", real_state.count())

real_state = clean.fillna(real_state, ['year_built', 'beds', 'baths', 'sqft', 'stories', 'listPrice', 'garage'])
print("Após preencher nulos:", real_state.count())

real_state = clean.removing_lines(real_state)
print("Após remover linhas:", real_state.count())

real_state = sqft_to_m2(real_state)
print("Após criar m2:", real_state.count())'''
    
    