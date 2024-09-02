import pandas as pd

def load_data(filename='covid_brasil.csv'):
    covid = pd.read_csv(filename, parse_dates=['data'])
    return covid

def analyze_data(covid):
    covid['obitos diarios'] = covid['obitos'].diff()
    covid['novas infecções'] = covid['confirmados'].diff()
    covid['% de óbitos'] = round(covid['obitos diarios'] / covid['novas infecções'], 4) * 100
    return covid

def calculate_moving_average(covid):
    media_mov = round(covid.groupby(pd.Grouper(key='data', freq="1W")).mean(), 3)
    media_mov = media_mov.drop(['confirmados', 'obitos', 'recuperados', 'ativos', '% de óbitos'], axis=1)
    return media_mov
