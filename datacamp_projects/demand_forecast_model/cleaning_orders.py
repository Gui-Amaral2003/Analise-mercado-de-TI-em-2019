## Importando as funções necessárias
from pyspark.sql import functions as F

def cleaning_orders(orders_data):
    ##Filtra os dados para os horarios fora de 12AM e 5AM
    orders_data = orders_data.filter((F.hour(orders_data['order_date']) >= 5))

    ##Categorizando os horarios
    orders_data = orders_data.withColumn('time_of_day', F.when((F.hour(orders_data['order_date']) >= 5) & (F.hour(orders_data['order_date']) <= 12), 'morning')
                                                        .when((F.hour(orders_data['order_date']) >= 12) & (F.hour(orders_data['order_date']) <= 18), 'afternoon')
                                                        .when((F.hour(orders_data['order_date']) >= 18), 'evening')
                                        )

    ##Fazendo o cast de timestamp para date
    orders_data = orders_data.withColumn("order_date", orders_data['order_date'].cast('date'))

    ##Limpando a coluna product

    ##Removendo as colunas que contem a palavra TV
    orders_data = orders_data.filter(~F.col('product').contains('TV'))

    ##Colocando a coluna em lowercase
    orders_data = orders_data.withColumn('product', F.lower(orders_data['product']))

    ##Limpando category

    ##Colocando em lowercase
    orders_data = orders_data.withColumn('category', F.lower(orders_data['category']))

    ## Criando a coluna purchase_state

    ##Separando a coluna por ',' e pegando a parte do estado e postal code
    orders_data = orders_data.withColumn('purchase_state', F.split(orders_data['purchase_address'], ",")[2])

    ##Separando o postal code do estado
    orders_data = orders_data.withColumn('purchase_state', F.split(orders_data['purchase_state'], " ")[1])

    return orders_data
