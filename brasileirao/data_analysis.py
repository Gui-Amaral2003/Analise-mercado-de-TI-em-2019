from math import nan
import data_cleaning
import pandas as pd


def porcentagem_de_vitorias(df:pd.DataFrame, time1:str, time2:str, retornar:bool = False):
    df_time1 = data_cleaning.separar_df_por_time(df, time1)
    
    # Filtrar os jogos entre os dois times
    df_time1_vs_time2 = df_time1[((df_time1['mandante'] == time1) & (df_time1['visitante'] == time2)) | 
                                 ((df_time1['mandante'] == time2) & (df_time1['visitante'] == time1))]

    # Verificar vitórias do time1 como mandante
    vitorias_mandante = (df_time1_vs_time2['mandante'] == time1) & (df_time1_vs_time2['vencedor'] == time1)

    # Verificar vitórias do time1 como visitante
    vitorias_visitante = (df_time1_vs_time2['visitante'] == time1) & (df_time1_vs_time2['vencedor'] == time1)
    
    ## Verificar os empates
    empates = (df_time1_vs_time2['vencedor'] == '-')
    
    
    ## Juntando ambas vitorias
    vitorias_time1 = vitorias_mandante | vitorias_visitante
    
    ## Obtendo as porcentagens
    num_vitorias = vitorias_time1.sum()
    num_empates = empates.sum()
    
    total_confrontos = len(df_time1_vs_time2)
    porcentagem_empates = (num_empates / total_confrontos) * 100
    porcentagem_vitorias = (num_vitorias / total_confrontos) * 100
    porcentagem_derrotas = 100 - (porcentagem_vitorias + porcentagem_empates)
    
    if(retornar):
        return porcentagem_vitorias, porcentagem_empates, porcentagem_derrotas
    else:
        print(f'Porcentagem de vitórias do {time1} sobre o {time2}: {porcentagem_vitorias:.2f}%, sendo {porcentagem_empates:.2f}% de empates')
        
        
def vantagem_gols(df:pd.DataFrame, time1:str, time2:str, retornar:bool = False):
    df_time1 = data_cleaning.separar_df_por_time(df, time1)
    
    # Filtrar os jogos entre os dois times
    df_time1_vs_time2 = df_time1[((df_time1['mandante'] == time1) & (df_time1['visitante'] == time2)) | 
                                 ((df_time1['mandante'] == time2) & (df_time1['visitante'] == time1))]
    
    # Garante que os dois times estão na Série A
    if(df_time1_vs_time2.empty):
        raise ValueError(f"Um dos times está na Série B!")
    
    # Obter os gols feitos pelo time1
    gols_vantagem = df_time1_vs_time2[df_time1_vs_time2['mandante'] == time1]['mandante_Placar'].sum() + \
                    df_time1_vs_time2[df_time1_vs_time2['visitante'] == time1]['visitante_Placar'].sum()
    
    # Obter os gols sofridos pelo time1
    gols_desvantagem = df_time1_vs_time2[df_time1_vs_time2['mandante'] == time2]['mandante_Placar'].sum() + \
                       df_time1_vs_time2[df_time1_vs_time2['visitante'] == time2]['visitante_Placar'].sum()
    
    if(retornar):
        return gols_vantagem, gols_desvantagem
    
    else:
        
        print(f"O {time1} possui um saldo de gols de {gols_vantagem - gols_desvantagem} contra o {time2}")
        
        
def desempenho_anual(df:pd.DataFrame, time1:str, time2:str, ano:int):
    df_ano = data_cleaning.limitar_ano(df, ano)
    
    vantagem_gols(df_ano, time1, time2)
    porcentagem_de_vitorias(df_ano, time1, time2)    
    
    
def desempenho_tecnico(df:pd.DataFrame, tecnico:str, time:str, retornar:bool = False):
    df_tec = data_cleaning.separar_df_por_tecnico(df, tecnico)
    
    df_tec = data_cleaning.separar_df_por_time(df_tec, time)
    
    # Verificar vitórias
    vitorias_mandante = df_tec[(df_tec['tecnico_mandante'] == tecnico) & 
                               (df_tec['vencedor'] == time) & 
                               (df_tec['mandante'] == time)]

    vitorias_visitante = df_tec[(df_tec['tecnico_visitante'] == tecnico) & 
                                (df_tec['vencedor'] == time) & 
                                (df_tec['visitante'] == time)]
    
    # Verificar derrotas
    derrotas_mandante = df_tec[(df_tec['tecnico_mandante'] == tecnico) & 
                               (df_tec['vencedor'] != time) & 
                               (df_tec['vencedor'] != '-') & 
                               (df_tec['mandante'] == time)]

    derrotas_visitante = df_tec[(df_tec['tecnico_visitante'] == tecnico) & 
                                (df_tec['vencedor'] != time) & 
                                (df_tec['vencedor'] != '-') & 
                                (df_tec['visitante'] == time)]
    
    ## Verificar os empates
    empates_mandante = df_tec[(df_tec['tecnico_mandante'] == tecnico) & 
                              (df_tec['vencedor'] == '-') & 
                              (df_tec['mandante'] == time)]
    
    empates_visitante = df_tec[(df_tec['tecnico_visitante'] == tecnico) & 
                               (df_tec['vencedor'] == '-') & 
                               (df_tec['visitante'] == time)]
    
    # contagem de resultados
    num_vitorias = len(vitorias_mandante) + len(vitorias_visitante)
    num_empates = len(empates_mandante) + len(empates_visitante)
    num_derrotas = len(derrotas_mandante) + len(derrotas_visitante)
    
    ## Obtendo as porcentagens
    total_confrontos = num_vitorias + num_empates + len(derrotas_mandante) + len(derrotas_visitante)
    porcentagem_empates = (num_empates / total_confrontos) * 100
    porcentagem_vitorias = (num_vitorias / total_confrontos) * 100
    porcentagem_derrotas = (num_derrotas / total_confrontos) * 100
    
    if(retornar):
        return porcentagem_vitorias, porcentagem_empates, porcentagem_derrotas
    else:
        print(f'O técnico: {tecnico} possui {porcentagem_vitorias:.2f}% de vitorias e {porcentagem_empates:.2f}% de empates')
    
    
def media_gols(df:pd.DataFrame, time):
    df = data_cleaning.separar_df_por_time(df, time)
    
    mandante = df[df['mandante'] == time]
    
    media = mandante['mandante_Placar'].mean()
    
    print(f'O {time} possui média de {media:.2f} gols como mandante')
    
    visitante = df[df['visitante'] == time]
    
    media_v = visitante['visitante_Placar'].mean()
    
    print(f'O {time} possui média de {media_v:.2f} gols como visitante')
    
    
   # Função para calcular a porcentagem de vitórias de um técnico contra o outro
def tecnico_vs_outro(df, tecnico_mandante, tecnico_visitante):
    total_jogos = len(df[(df['tecnico_mandante'] == tecnico_mandante) & (df['tecnico_visitante'] == tecnico_visitante)])
    vitorias_mandante = len(df[(df['tecnico_mandante'] == tecnico_mandante) & (df['tecnico_visitante'] == tecnico_visitante) & (df['vencedor'] == df['mandante'])])
    vitorias_visitante = len(df[(df['tecnico_mandante'] == tecnico_mandante) & (df['tecnico_visitante'] == tecnico_visitante) & (df['vencedor'] == df['visitante'])])
    
    if total_jogos > 0:
        porcentagem_vitorias_mandante = (vitorias_mandante / total_jogos) * 100
        porcentagem_vitorias_visitante = (vitorias_visitante / total_jogos) * 100
    else:
        porcentagem_vitorias_mandante = 0
        porcentagem_vitorias_visitante = 0
    
    return porcentagem_vitorias_mandante, porcentagem_vitorias_visitante

def time_vs_outro(df, time_mandante, time_visitante):
    total_jogos = len(df[(df['mandante'] == time_mandante) & (df['visitante'] == time_visitante)])
    vitorias_mandante = len(df[(df['mandante'] == time_mandante) & (df['visitante'] == time_visitante) & (df['vencedor'] == df['mandante'])])
    vitorias_visitante = len(df[(df['mandante'] == time_mandante) & (df['visitante'] == time_visitante) & (df['vencedor'] == df['visitante'])])
    
    if total_jogos > 0:
        porcentagem_vitorias_mandante = (vitorias_mandante / total_jogos) * 100
        porcentagem_vitorias_visitante = (vitorias_visitante / total_jogos) * 100
    else:
        porcentagem_vitorias_mandante = 0
        porcentagem_vitorias_visitante = 0
    
    return porcentagem_vitorias_mandante, porcentagem_vitorias_visitante

def desempenho_time_no_estadio(df: pd.DataFrame, time: str, estadio: str):
    # Filtrar os jogos em que o time jogou como mandante no estádio
    df_time_estadio = df[(df['mandante'] == time) & (df['arena'] == estadio)]
    
    # Verificar vitórias como mandante no estádio
    vitorias = df_time_estadio[df_time_estadio['vencedor'] == time]
    
    # Verificar derrotas como mandante no estádio
    derrotas = df_time_estadio[(df_time_estadio['vencedor'] != time) & (df_time_estadio['vencedor'] != '-')]
    
    # Verificar empates como mandante no estádio
    empates = df_time_estadio[df_time_estadio['vencedor'] == '-']
    
    # Contagem de resultados
    num_jogos = len(df_time_estadio)
    num_vitorias = len(vitorias)
    num_derrotas = len(derrotas)
    num_empates = len(empates)
    
    # Verificar se há jogos no estádio para evitar divisão por zero
    if num_jogos == 0:
        return 0, 0, 0
    
    # Calcular as porcentagens
    porcentagem_vitorias = (num_vitorias / num_jogos) * 100
    porcentagem_empates = (num_empates / num_jogos) * 100
    porcentagem_derrotas = (num_derrotas / num_jogos) * 100
    
    return porcentagem_vitorias, porcentagem_empates, porcentagem_derrotas    
    
    
    
    
    
    
