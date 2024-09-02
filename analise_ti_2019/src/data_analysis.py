import pandas as pd

def analyze_age_distribution(df: pd.DataFrame):
    age = df["('P1', 'age')"].value_counts()
    age_common = age.iloc[0:5]
    return age_common

def analyze_exterior_percentage(df: pd.DataFrame):
    ext = df["('P3', 'living_in_brasil')"][df["('P3', 'living_in_brasil')"] == 0].count()
    all_e = df["('P3', 'living_in_brasil')"].count()
    ext_porc = round((ext * 100) / all_e, 2)
    return ext_porc

def analyze_state_percentage(df: pd.DataFrame):
    all_est = df["('P5', 'living_state')"].count()
    qnt_est = df["('P5', 'living_state')"].value_counts()
    porc_est = round((qnt_est * 100) / all_est, 2)
    return porc_est

def analyze_gender_discrepancy(df: pd.DataFrame):
    masc = df["('P2', 'gender')"][df["('P2', 'gender')"] == "Masculino"].count()
    all_g = df["('P2', 'gender')"].count()
    porc_masc = round((masc * 100) / all_g, 2)
    porc_fem = 100 - porc_masc 
    return porc_masc, porc_fem

def analyze_management_gender_discrepancy(df: pd.DataFrame):
    all_mang = df[df["('P13', 'manager')"] == 1.0]
    fem_mang = all_mang["('P2', 'gender')"][all_mang["('P2', 'gender')"] == "Feminino"].count()
    porc_fem_mang = round((fem_mang * 100) / all_mang["('P13', 'manager')"].count(), 2)
    porc_mas_mang = 100 - porc_fem_mang
    return porc_fem_mang, porc_mas_mang

def analyze_intern_salary(df: pd.DataFrame):
    estag = df[df["('P10', 'job_situation')"] == "Estagiário"]
    estag_sal_base = estag["('P16', 'salary_range')"][estag["('P16', 'salary_range')"] == "de R$ 1.001/mês a R$ 2.000/mês"].count()
    estag_sal_base_porc = round((estag_sal_base * 100) / estag["('P10', 'job_situation')"].count(), 2)

    estag_fem = estag[estag["('P2', 'gender')"] == "Feminino"]
    estag_sal_base_fem = estag_fem["('P16', 'salary_range')"][estag_fem["('P16', 'salary_range')"] == "de R$ 1.001/mês a R$ 2.000/mês"].count()
    estag_sal_base_fem_porc = round((estag_sal_base_fem * 100) / estag_sal_base, 2)

    return estag_sal_base_porc, estag_sal_base_fem_porc

