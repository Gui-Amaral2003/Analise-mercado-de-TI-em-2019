from sklearn.metrics import accuracy_score
import machineLearning
import data_fetch
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
df = data_fetch.fetch_data()

X_train, X_test, y_train, y_test = machineLearning.preparar_df(df)
model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print("MSE: ", mse)





