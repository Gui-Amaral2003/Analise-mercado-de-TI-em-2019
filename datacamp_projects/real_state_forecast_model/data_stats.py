import data_fetch as df
import matplotlib.pyplot as plt
import pandas as pd

real_state = df.fetch_data(type = 'pandas')
'''
type_count = real_state['type'].value_counts()
plt.bar(type_count.index, type_count.values)
plt.xlabel('Tipo da casa')
plt.xticks(rotation = 25)
plt.ylabel('Quantidade')
plt.show()
'''

print(real_state[['baths', 'garage', 'stories', 'lot_sqft', 'sqft']].describe())

##Podemos observar valores suspeitos: como casa com 400 vagas de carro e 119 andares. Essas linhas serão removidas posteriormente.

print(real_state.isnull().sum())

##Podemos observar que quase metade dos lot_sqft e baths_half são nulls, logo a coluna sera deletada.