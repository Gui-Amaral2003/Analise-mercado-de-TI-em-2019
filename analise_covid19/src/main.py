# main.py
from data_fetch import fetch_covid_data, format_covid_data
from data_process import process_dates, save_to_csv
from data_analysis import load_data, analyze_data, calculate_moving_average
from visualization import med_mov_graph, plot_vaccine_dates

# Fetch and process data
raw_data = fetch_covid_data()
formatted_data = format_covid_data(raw_data)
processed_data = process_dates(formatted_data)
save_to_csv(processed_data)

# Analyze data
covid_data = load_data()
covid_analyzed = analyze_data(covid_data)
media_mov = calculate_moving_average(covid_analyzed)

# Visualize data
med_mov_graph(media_mov, covid_analyzed)
med_mov_graph(media_mov, covid_analyzed, col_med='novas infecções', col_cov='novas infecções', legend=['Média móvel das infecções', 'Novas infecções'], title='Novas infecções da COVID-19 no Brasil')
plot_vaccine_dates(covid_analyzed)
