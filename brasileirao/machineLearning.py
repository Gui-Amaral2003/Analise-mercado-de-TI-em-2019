import pandas as pd
import data_cleaning
import data_fetch
import data_analysis
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = data_fetch.fetch_data()
df = data_cleaning.separar_df_por_time(df, 'Palmeiras')
# Função para preparar os dados
def preparar_dados(df):
    
    # Função para aplicar a técnica e extrair as porcentagens de vitórias e empates
    df['porcentagem_vitorias_tecnico_mandante'], df['porcentagem_vitorias_tecnico_visitante'] = zip(*df.apply(lambda row: 
       data_analysis.tecnico_vs_outro(df, row['tecnico_mandante'], row['tecnico_visitante']), axis=1))
    
    df['porcentagem_vitorias_mandante'], df['porcentagem_vitorias_visitante'] = zip(*df.apply(lambda row: 
       data_analysis.time_vs_outro(df, row['mandante'], row['visitante']), axis=1))
    
    
    
    # Seleção de features relevantes (pode ajustar conforme a relevância)
    features = ['mandante', 'visitante', 'porcentagem_vitorias_tecnico_mandante', 'porcentagem_vitorias_visitante', 
                'porcentagem_vitorias_mandante']
    
    
    
    # Separar features (X) e targets (y)
    X = df[features]
    y_mandante = df['mandante_Placar']
    y_visitante = df['visitante_Placar']
    
    # One-hot encoding para colunas categóricas
    encoder = OneHotEncoder()
    X_encoded = encoder.fit_transform(X)
    
    # Dividir os dados em treinamento e teste
    X_train, X_test, y_train_mandante, y_test_mandante = train_test_split(X_encoded, y_mandante, test_size=0.3, random_state=42)
    X_train, X_test, y_train_visitante, y_test_visitante = train_test_split(X_encoded, y_visitante, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train_mandante, y_test_mandante, y_train_visitante, y_test_visitante

# Função para treinar o modelo e prever placares
def treinar_modelo(X_train, y_train, X_test):
    # Modelo: RandomForest para prever gols do mandante e do visitante
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Treinamento
    modelo.fit(X_train, y_train)
    
    # Previsão
    y_pred = modelo.predict(X_test)
    
    return modelo, y_pred

# Função principal
def prever_placar(df):
    # Preparar dados
    X_train, X_test, y_train_mandante, y_test_mandante, y_train_visitante, y_test_visitante = preparar_dados(df)
    
    # Treinar modelos para placar do mandante e visitante
    modelo_mandante, y_pred_mandante = treinar_modelo(X_train, y_train_mandante, X_test)
    modelo_visitante, y_pred_visitante = treinar_modelo(X_train, y_train_visitante, X_test)
    
    # Avaliação
    mse_mandante = mean_squared_error(y_test_mandante, y_pred_mandante)
    mse_visitante = mean_squared_error(y_test_visitante, y_pred_visitante)
    
    print(f"Erro quadrático médio - Mandante: {mse_mandante}")
    print(f"Erro quadrático médio - Visitante: {mse_visitante}")
    
    # Podemos também retornar as previsões dos placares
    return y_pred_mandante, y_pred_visitante

# Suponha que df seja o DataFrame contendo os dados do jogo
# Prever placares
y_pred_mandante, y_pred_visitante = prever_placar(df)

'''
# Exibir as previsões
for i in range(len(y_pred_mandante)):
    print(f"Previsão do placar: Mandante {y_pred_mandante[i]:.0f} x Visitante {y_pred_visitante[i]:.0f}")
'''

##erro pré-tratamento: Erro quadrático médio - Mandante: 1.6941160275634481 Erro quadrático médio - Visitante: 1.2317386673737258
