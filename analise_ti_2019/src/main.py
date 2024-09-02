from data_fetch import fetch_data
from data_analysis import (
    analyze_age_distribution, 
    analyze_exterior_percentage, 
    analyze_state_percentage, 
    analyze_gender_discrepancy, 
    analyze_management_gender_discrepancy, 
    analyze_intern_salary
)
from visualization import plot_state_distribution

url = "https://drive.google.com/file/d/1jq9LFaAVQrQIn6la5F1ioU8gAfkJwUiY/view?usp=sharing"
df = fetch_data(url)

# Executar análises
age_common = analyze_age_distribution(df)
print(age_common)

ext_porc = analyze_exterior_percentage(df)
print(f"Aproximadamente {ext_porc}% dos brasileiros que trabalham com análise de dados moram no exterior")

porc_est = analyze_state_percentage(df)
print(porc_est)

plot_state_distribution()

porc_masc, porc_fem = analyze_gender_discrepancy(df)
print(f"{porc_masc}% de quem trabalha na área são homens e {porc_fem}% são mulheres")

porc_fem_mang, porc_mas_mang = analyze_management_gender_discrepancy(df)
print(f"Porcentagem de gerentes que são mulheres: {porc_fem_mang}% e porcentagem que são homens: {porc_mas_mang}%")

estag_sal_base_porc, estag_sal_base_fem_porc = analyze_intern_salary(df)
print(f"{estag_sal_base_porc}% dos estagiários recebem entre mil e dois mil Reais, entre esses estagiários, {estag_sal_base_fem_porc}% são mulheres")
