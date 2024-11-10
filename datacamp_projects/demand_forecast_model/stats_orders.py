from pyspark.sql.functions import avg, month, dayofweek
from pyspark.sql.window import Window

def moving_average(df):
    ##Criando a janela que a media movel atuara
    window = Window.partitionBy('product').orderBy('order_date')
    
    df.withColumn('moving_average', avg('quantity_ordered').over(window))
    
    return df

def time_features(df):
    df = df.withColumn("month", month("order_date"))
    df = df.withColumn("day_of_week", dayofweek("order_date"))
    
    return df