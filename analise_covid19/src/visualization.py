import matplotlib.pyplot as plt
import numpy as np

def med_mov_graph(media_mov, covid, col_med='obitos diarios', col_cov='obitos diarios', legend=None, title='Mortes da COVID-19 no Brasil'):
    if legend is None:
        legend = ['Média móvel dos óbitos', 'Óbitos diários']
    plt.plot(media_mov.index, media_mov[col_med], color='black')
    plt.bar(covid['data'], covid[col_cov], color='grey')
    plt.legend(legend)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

def plot_vaccine_dates(covid):
    vacina_data1 = np.datetime64('2021-01-17')
    vacina_data2 = np.datetime64('2021-07-08')
    vacina_data3 = np.datetime64('2021-08-13')
    plt.figure(figsize=(8, 6))
    plt.bar(covid['data'], covid['obitos diarios'], color='grey')
    plt.xticks(rotation=45)
    plt.axvline(vacina_data1, color='red', linestyle='--')
    plt.axvline(vacina_data2, color='blue', linestyle='--')
    plt.axvline(vacina_data3, color='green', linestyle='--')
    plt.legend(['Aplicação da primeira dose', 'Aplicação entre 37 a 39 anos', 'Aplicação entre 18 a 24 anos'])
    plt.title('Relação entre vacinas e óbitos diários')
    plt.show()
