import pandas as pd
import matplotlib.pyplot as plt

url = "https://drive.google.com/file/d/1jq9LFaAVQrQIn6la5F1ioU8gAfkJwUiY/view?usp=sharing"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]

df = pd.read_csv(url)

## Idade mais comuns entre os interessados em data science

age = df["('P1', 'age')"].value_counts()
age_common = age.iloc[0:5]
print(age_common)

## Porcentagem que mora no exterior

ext = df["('P3', 'living_in_brasil')"][df["('P3', 'living_in_brasil')"] == 0].count()
all_e = df["('P3', 'living_in_brasil')"].count()
ext_porc = round((ext * 100) / all_e, 2)
print(f"Aproximadamente {ext_porc}% dos brasileiros que trabalham com analise de dados moram no exterior")

## Porcentagem de pessoas de cada estado

all_est = df["('P5', 'living_state')"].count()
qnt_est = df["('P5', 'living_state')"].value_counts()
porc_est = round((qnt_est *100) / all_est, 2)
print(porc_est)

## Gráfico da porcentagem dos estados
labels = ["SP", "MG", "RJ", "PR", "SC", "RS", "ES"]
sizes = [46.85, 22.13, 10.29, 8.19, 5.81, 4.83, 1.89]
explode = (0, 0, 0, 0, 0, 0, 0.1) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, pctdistance=0.8)
ax1.axis('equal') 
plt.show()

## A discrepância de gênero que essa área possui

masc = df["('P2', 'gender')"][df["('P2', 'gender')"] == "Masculino"].count()
all_g = df["('P2', 'gender')"].count()
porc_masc = round((masc * 100) / all_g, 2)
porc_fem = 100 - porc_masc 
print(f"{porc_masc}% de quem trabalha na área são homens e {porc_fem}% de mulheres")

## A porcentagem de generos quando se trata de cargos de gestão se mantem 

all_mang = df[df["('P13', 'manager')"] == 1.0]
fem_mang = all_mang["('P2', 'gender')"][all_mang["('P2', 'gender')"] == "Feminino"].count()
porc_fem_mang = round((fem_mang * 100) / all_mang["('P13', 'manager')"].count(), 2)
porc_mas_mang = 100 - porc_fem_mang
print(f"Porcentagem de gerentes que são mulheres: {porc_fem_mang}% e porcentagem que são homens: {porc_mas_mang}%")

## Base salarial do estagiário

estag = df[df["('P10', 'job_situation')"] == "Estagiário"]
estag_sal_base = estag["('P16', 'salary_range')"][estag["('P16', 'salary_range')"] == "de R$ 1.001/mês a R$ 2.000/mês"].count()
estag_sal_base_porc = round((estag_sal_base * 100) / estag["('P10', 'job_situation')"].count(), 2)

## Estagiarios que recebem entre 1K-2K e que são mulheres

estag_fem = estag[estag["('P2', 'gender')"] == "Feminino"]
estag_sal_base_fem = estag_fem["('P16', 'salary_range')"][estag_fem["('P16', 'salary_range')"] == "de R$ 1.001/mês a R$ 2.000/mês"].count()
estag_sal_base_fem_porc = round((estag_sal_base_fem * 100) / estag_sal_base)
print(f"{estag_sal_base_porc}% dos estagiários recebem entre mil e dois mil Reais, entre esses estagiários, {estag_sal_base_fem_porc}% são mulheres")