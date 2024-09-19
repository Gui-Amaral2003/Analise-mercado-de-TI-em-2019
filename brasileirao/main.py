import data_fetch
import data_cleaning
import pandas as pd
df = data_fetch.fetch_data()

tecnico2 = 'A. Moreira Ferreira'
tecnico = 'L. Venker de Menezes'
time = 'Palmeiras'

df = data_cleaning.separar_df_por_tecnico(df, tecnico)

df = data_cleaning.separar_df_por_tecnico(df, tecnico2)

print(df.columns)





