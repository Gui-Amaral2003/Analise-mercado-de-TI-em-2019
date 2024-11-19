import data_fetch as df
import matplotlib.pyplot as plt
import pandas as pd

real_state = df.fetch_data(type = 'pandas')

type_count = real_state['type'].value_counts()
plt.bar(type_count.index, type_count.values)
plt.xlabel('Tipo da casa')
plt.xticks(rotation = 25)
plt.ylabel('Quantidade')

description = round(real_state[['baths', 'garage', 'stories', 'lot_sqft', 'sqft']].describe(), 2)

fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=description.values, colLabels=description.columns, rowLabels=description.index, loc='center')
plt.show()

##Podemos observar valores suspeitos: como casa com 400 vagas de carro e 119 andares. Essas linhas serão removidas posteriormente.

