# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
between = np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)
medium = cars[between]

# Print medium
print(medium)

'''
O código acima filtra o DataFrame 'cars' para identificar observações onde o número de carros per capita ('cars_per_cap') está entre 100 e 500. Primeiro, ele utiliza a função 'np.logical_and' do NumPy para criar uma Série booleana 'between' que verifica se os valores em 'cars_per_cap' são maiores que 100 e menores que 500. Em seguida, essa Série booleana é usada para filtrar o DataFrame 'cars', resultando em um novo DataFrame chamado 'medium', que contém apenas as linhas que atendem a essa condição. Finalmente, o código imprime o DataFrame filtrado 'medium', mostrando os países com um número médio de carros per capita.
'''