##TODO: Analisar a quantidade de vitorias do palmeiras nesses 20 anos. Analisar a quantidade de vitorias do Palmeiras em cima do Corinthians. 
import data_fetch
import data_analysis
import data_cleaning
import pandas as pd
df = data_fetch.fetch_data()
df_palmeiras = data_cleaning.separar_df_por_time(df, 'Palmeiras')

anos = [i for i in range(2003, 2024)]

'''
for i in anos:
    print(f'\n{i}')
    try:
        data_analysis.desempenho_anual(df, 'Palmeiras', 'Corinthians', i)
    except ValueError as e:
        print(e)


## Desempenho de tecnicos com mais de 20 jogos 

contagem_visitante = df_palmeiras['tecnico_visitante'].value_counts()
contagem_mandante = df_palmeiras['tecnico_mandante'].value_counts()

# Somar as contagens das duas colunas
contagem_total = contagem_visitante.add(contagem_mandante, fill_value=0)

# Filtrar os técnicos que aparecem mais de 20 vezes no total
tecnicos_filtrados = contagem_total[contagem_total > 15].index

tecnicos = tecnicos_filtrados.to_list()

for tecnico in tecnicos:
    print(f'\n{tecnico}')
    
    data_analysis.desempenho_tecnico(df_palmeiras, tecnico, 'Palmeiras')
    
## Média de gols em casa 
data_analysis.media_gols(df, 'Palmeiras')
'''