import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\food_consumption.csv', index_col=0)

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))

# Histogram of co2_emission for rice and show plot
rice_consumption['co2_emission'].hist()
plt.show()

'''
O código acima demonstra como calcular medidas de tendência central (média e mediana) para as emissões de CO2 associadas ao consumo de arroz, além de visualizar a distribuição dessas emissões por meio de um histograma. A média e a mediana fornecem insights sobre o valor típico das emissões, enquanto o histograma ajuda a entender a dispersão e a forma da distribuição dos dados.
'''