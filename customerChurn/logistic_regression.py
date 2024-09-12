import machineLearning
import data_fetch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


df = data_fetch.fetch_data()

X_train, X_test, y_train, y_test = machineLearning.preparar_df(df)

param_grid = {"C": [0.1, 1, 10],
              "solver":["liblinear", "lbfgs"],
              "class_weight": [None, "balanced"]}

model = LogisticRegression()
grid = GridSearchCV(model, param_grid, cv = 5)

grid.fit(X_train, y_train)

print("Melhores parâmetros encontrados:", grid.best_params_)

melhor_modelo = grid.best_estimator_

y_pred = melhor_modelo.predict(X_test)

precisao = accuracy_score(y_test, y_pred)
print(f"Precisão da regressão linear: {precisao}")