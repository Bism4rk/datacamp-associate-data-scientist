# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

'''
O código acima filtra o DataFrame 'cars' para identificar observações onde o número de carros per capita ('cars_per_cap') é superior a 500. Primeiro, ele extrai a coluna 'cars_per_cap' como uma Série chamada 'cpc'. Em seguida, cria uma Série booleana 'many_cars' que indica quais valores em 'cpc' são maiores que 500. Usando essa Série booleana, o código filtra o DataFrame 'cars' para criar um novo DataFrame chamado 'car_maniac', que contém apenas as linhas onde a condição é verdadeira. Finalmente, ele imprime o DataFrame filtrado 'car_maniac', mostrando os países com mais de 500 carros per capita.
'''