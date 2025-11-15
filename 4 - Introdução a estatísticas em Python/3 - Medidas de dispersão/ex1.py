import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\food_consumption.csv', index_col=0)

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
plt.figure()
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist();
plt.show()

'''
O código acima demonstra como calcular a variância e o desvio padrão das emissões de CO2 para diferentes categorias de alimentos usando o pandas. Além disso, ele cria histogramas para visualizar a distribuição das emissões de CO2 para as categorias 'beef' e 'eggs'. A variância e o desvio padrão são medidas importantes de dispersão que ajudam a entender a variabilidade dos dados em cada categoria alimentar.
'''