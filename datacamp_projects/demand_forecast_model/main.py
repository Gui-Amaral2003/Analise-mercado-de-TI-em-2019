import datacamp_projects.demand_forecast_model.data_fetch as fd
import cleaning_orders as co
import stats_orders as so
from pyspark.sql import SparkSession

from datacamp_projects.demand_forecast_model.stats_orders import moving_average
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