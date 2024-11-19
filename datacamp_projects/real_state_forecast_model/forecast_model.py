import data_fetch as df
import features as feat
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, StandardScaler, VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

real_state = df.fetch_data()
real_state = feat.prepare_df(real_state)


indexer = StringIndexer(inputCol='type', outputCol='type_idx')
encoder = OneHotEncoder(inputCol=indexer.getOutputCol(), outputCol='type_vec')

assembler = VectorAssembler(inputCols=['year_built', 
                                       'beds', 
                                       'baths', 
                                       'garage', 
                                       'm2',
                                       'is_large_home',
                                       'luxury_indicator',
                                       'baths_to_m2', 
                                       'baths_to_beds', 
                                       'baths_to_stories', 
                                       'beds_to_m2', 
                                       'beds_to_stories', 
                                       'garage_to_m2',
                                       'type_vec'], outputCol='features')

scaler = StandardScaler(inputCol='features', outputCol='scaled_features', withStd=True, withMean=False)

pipe = Pipeline(stages=[indexer, encoder, assembler, scaler])

pipeline_model = pipe.fit(real_state)

real_state_transformed = pipeline_model.transform(real_state)

train_data, test_data = real_state_transformed.randomSplit([0.75, 0.25], seed = 43)

regression = LinearRegression(featuresCol='scaled_features', labelCol='listPrice')

grid = (ParamGridBuilder()
             .addGrid(regression.regParam, [0.01, 0.1, 1.0])  
             .addGrid(regression.elasticNetParam, [0.0, 0.5, 1.0])  
             .build())

evaluator = RegressionEvaluator(labelCol='listPrice', predictionCol='prediction', metricName='rmse')
crossval = CrossValidator(estimator=regression, estimatorParamMaps=grid, evaluator=evaluator, numFolds=3)


##Treinamento do modelo
cv_model = crossval.fit(train_data)

##Melhor modelo
best_model = cv_model.bestModel
best_prediction = best_model.transform(test_data)

##Acessando a avaliação do melhor modelo
rmse = evaluator.evaluate(best_prediction)

print(rmse) ##641170