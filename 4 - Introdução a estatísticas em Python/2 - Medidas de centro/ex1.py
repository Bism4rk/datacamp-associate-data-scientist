import pandas as pd
import numpy as np

food_consumption = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\food_consumption.csv', index_col=0)

# Subset country for USA: usa_consumption
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean consumption in USA
print(np.mean(usa_consumption['consumption']))

# Calculate median consumption in USA
print(np.median(usa_consumption['consumption']))

'''
O código acima demonstra como carregar um conjunto de dados sobre consumo de alimentos e calcular medidas de tendência central, como a média e a mediana, para o consumo nos Estados Unidos. Primeiro, o conjunto de dados é carregado usando pandas, e em seguida, é criado um subconjunto que contém apenas os dados referentes aos EUA. Finalmente, a média e a mediana do consumo são calculadas e impressas na tela.
'''