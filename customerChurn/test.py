import data_analysis
import data_fetch
import pandas as pd
import numpy as np

df = data_fetch.fetch_data()

print(data_analysis.porcentagem_valor(df))