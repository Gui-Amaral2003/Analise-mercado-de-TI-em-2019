import datetime as dt
import csv

def process_dates(f_data):
    for ind in range(1, len(f_data)):
        f_data[ind][4] = dt.datetime.strptime(f_data[ind][4], '%Y-%m-%dT%H:%M:%SZ')
    return f_data

def save_to_csv(f_data, filename='covid_brasil.csv'):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(f_data)
