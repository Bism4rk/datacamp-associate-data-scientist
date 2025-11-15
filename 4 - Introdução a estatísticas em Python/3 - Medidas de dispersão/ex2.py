import pandas as pd
import numpy as np

food_consumption = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\food_consumption.csv', index_col=0)

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 5)))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))

'''
O código acima demonstra como calcular os quartis, quintis e decis das emissões de CO2 usando a função `np.quantile` do NumPy. Essas medidas de posição ajudam a entender a distribuição dos dados, dividindo-os em partes iguais. Quartis dividem os dados em quatro partes, quintis em cinco partes e decis em dez partes, fornecendo uma visão detalhada da dispersão dos valores de emissão de CO2 no conjunto de dados.
'''