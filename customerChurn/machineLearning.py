import pandas as pd
import data_fetch
import data_cleaning
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def preparar_df(df:pd.DataFrame):
    df = data_fetch.fetch_data()

    df = data_cleaning.remover_duplicatas(df)

    y = df["Churn"]
    X  = data_cleaning.remover_coluna(df, coluna = ["Age Group", "Age", "Churn"])

    X = scale(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, stratify = y, random_state = 42)
    return X_train, X_test, y_train, y_test

##TODO: Implementar os modelos de ML que suportam o train test split