import requests as r

def fetch_covid_data(url='https://api.covid19api.com/dayone/country/brazil'):
    resp = r.get(url)
    r_data = resp.json()
    return r_data

def format_covid_data(r_data):
    f_data = []
    for i in r_data:
        f_data.append([i['Confirmed'], i['Deaths'], i['Recovered'], i['Active'], i['Date']])
    f_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])
    return f_data
