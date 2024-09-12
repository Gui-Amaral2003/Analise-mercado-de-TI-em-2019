import data_analysis
import data_fetch
import pandas as pd
import numpy as np

df = data_fetch.fetch_data()

nome = data_analysis.valor_mais_comum(df, "Status")

age_groups = [i for i in range(0, 6)]
calls = []
sms = []
sms_percentage = []
for i in age_groups:
    df_age = data_analysis.separar_df(df, "Age Group", i)
    calls.append(data_analysis.somar_coluna(df_age, "Frequency of use"))
    sms.append(data_analysis.somar_coluna(df_age, "Frequency of SMS"))
    if(calls[i] != 0):
        sms_percentage.append(round((sms[i] / (calls[i] + sms[i])) * 100, 2))
    else:
        sms_percentage.append(np.float64(0))
    
df_sms_usage = pd.DataFrame({
    "Grupo": age_groups,
    "Total de ligações": calls,
    "Total de SMS": sms,
    "Porcentagem de SMS": sms_percentage,
})

print(df_sms_usage)

data_analysis.correlacao(df, "Churn")


    






