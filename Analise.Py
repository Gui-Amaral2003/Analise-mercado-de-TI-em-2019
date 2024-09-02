import requests as r

url = 'https://api.covid19api.com/dayone/country/brazil'

resp = r.get(url)
r_data = resp.json()

f_data = []

for i in r_data:
    f_data.append([i['Confirmed'], i['Deaths'], i['Recovered'], i['Active'], i['Date']])
    
f_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])

import datetime as dt
import csv
for ind in range(1, len(f_data)):
    f_data[ind][4] = dt.datetime.strptime(f_data[ind][4], '%Y-%m-%dT%H:%M:%SZ')
    
with open('covid_brasil.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(f_data)

import pandas as pd
import numpy as np
covid = pd.read_csv('covid_brasil.csv', parse_dates = ['data'])
#covid['data'] = pd.to_datetime(covid['data'], format = '%Y-%m-%d %H:%M:%S')
print(covid.info())
covid.tail(2)

covid['obitos diarios'] = covid['obitos'].diff()
covid['novas infecções'] = covid['confirmados'].diff()
covid['% de óbitos'] = round(covid['obitos diarios'] / covid['novas infecções'], 4) * 100
covid.tail()

media_mov = round(covid.groupby(pd.Grouper(key = 'data', freq="1W")).mean(), 3)

media_mov = media_mov.drop(['confirmados', 'obitos', 'recuperados', 'ativos', '% de óbitos'], axis=1)

media_mov

import matplotlib.pyplot as plt

def med_mov_graph(col_med = 'obitos diarios', col_cov = 'obitos diarios', legend = ['Média móvel dos óbitos', 'Óbitos diários'], title = 'Mortes da COVID-19 no Brasil'):
    plt.plot(media_mov.index, media_mov[col_med], color = 'black')
    plt.bar(covid['data'], covid[col_cov], color = 'grey')
    plt.legend([f'Média móvel {col_med}', f'{col_med}'])
    plt.title(title)
    plt.xticks(rotation = 45)
    plt.show()
    
med_mov_graph()
med_mov_graph(col_med = 'novas infecções', col_cov = 'novas infecções', legend = ['Média móvel das infecções', 'Novas infecções'], title = 'Novas infecções da COVID-19 no Brasil')

#Datas baseado no cronograma do estado de São Paulo

vacina_data1 = np.datetime64('2021-01-17')
vacina_data2 = np.datetime64('2021-07-08')
vacina_data3 = np.datetime64('2021-08-13')
plt.figure(figsize = (8, 6))
plt.bar(covid['data'], covid['obitos diarios'], color = 'grey')
plt.xticks(rotation = 45)
plt.axvline(vacina_data1, color = 'red', linestyle = '--')
plt.axvline(vacina_data2, color = 'blue', linestyle = '--')
plt.axvline(vacina_data3, color = 'green', linestyle = '--')
plt.legend(['Aplicação da primeria dose', 'Aplicação entre 37 a 39 anos', 'Aplicação entre 18 a 24 anos'])
plt.title('Relação entre vacinas e óbitos diários')
plt.show()

def anos(ano):
    covid_ano = covid.copy()
    covid_ano['data'] = covid_ano['data'].dt.year
    df = covid_ano[covid_ano['data'] == ano]
    return df

def dados_anos(ano, coluna, op = 'mean'):
    a = list(ano)

    if op == 'mean':
        for i in a:
            df = anos(i)
            res = df[coluna].mean()
            print(f'O ano {i} possui uma média de {coluna} de {res}\n')
            
    elif op == 'median':
        for i in a:
            df = anos(i)
            res = df[coluna].median()
            print(f'O ano {i} possui uma mediana de {coluna} de {res}\n')
    elif op == 'max' or op == 'min':
        for i in a:
            df = anos(i)
            df = df.fillna(0)
            res_max = max(df[coluna])
            res_min = min(df[coluna])
            if res_min < 0:
                res_min = 0
            print(f'O ano {i} possui o valor máximo de {coluna} igual a {res_max} e o valor minímo de {res_min}\n')
    else:
        print('operação ainda não suportada')

dados_anos([2020, 2021, 2022], '% de óbitos', 'median')

dados_anos([2020, 2021, 2022], 'novas infecções', 'mean')