from pyspark.ml.feature import VectorAssembler, OneHotEncoder, StringIndexer
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline

import data_fetch as fd
import cleaning_orders as co
import stats_orders as so
from pyspark.sql import SparkSession
import stats_orders as so

##Iniciando a sessão do Spark
spark = (
    SparkSession
    .builder
    .appName('cleaning_orders_dataset_with_pyspark')
    .getOrCreate()
)

orders_data = spark.createDataFrame(fd.fetch_data())
orders_data = co.cleaning_orders(orders_data)
orders_data = so.moving_average(orders_data)
orders_data = so.time_features(orders_data)

##Realizando o OneHotEncode nas colunas necessarias

tod_indexer = StringIndexer(inputCol="time_of_day", outputCol="time_of_day_idx")
tod_encoder = OneHotEncoder(inputCol=tod_indexer.getOutputCol(), outputCol="time_of_day_vec")

ps_indexer = StringIndexer(inputCol= "purchase_state", outputCol="purchase_state_idx")
ps_encoder = OneHotEncoder(inputCol=ps_indexer.getOutputCol(), outputCol="purchase_state_vec")

##Separando as features
assembler = VectorAssembler(inputCols= ["price_each", 
                                        'time_of_day_vec', 
                                        "purchase_state_vec", 
                                        "month", 
                                        "day_of_week"], outputCol="features")

pipe = Pipeline(stages = [ps_indexer, tod_indexer, ps_encoder, tod_encoder, assembler])

pipeline = pipe.fit(orders_data)

orders_transformed = pipeline.transform(orders_data)

train_data, test_data = orders_transformed.randomSplit([0.75, 0.25], seed = 43)

##Aplicando o modelo

forest = RandomForestRegressor(featuresCol='features', labelCol='quantity_ordered')

'''forest_model = forest.fit(train_data)

predictions = forest_model.transform(test_data)

evaluator = RegressionEvaluator(labelCol='quantity_ordered', predictionCol='prediction', metricName='rmse')
rmse = evaluator.evaluate(predictions)

print(f"RMSE: {rmse}") ##0.411'''

evaluator = RegressionEvaluator(labelCol='quantity_ordered', predictionCol='prediction', metricName='rmse')
##Melhorando o modelo

from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

#Definindo o ParamGrid

grid = ParamGridBuilder().addGrid(forest.numTrees, [100, 200, 300]) \
                        .addGrid(forest.maxDepth, [5, 10, 15]) \
                        .build()
                        
##Definindo o crossvalidator

crossval = CrossValidator(estimator = forest, estimatorParamMaps=grid, evaluator = evaluator, numFolds = 3)

##Treinamento do modelo
cv_model = crossval.fit(train_data)

##Melhor modelo
best_model = cv_model.bestModel
best_prediction = best_model.transform(test_data)

##Acessando a avaliação do melhor modelo
rmse = evaluator.evaluate(best_prediction)

print("Melhor modelo:", best_model)
print("RMSE:", rmse)