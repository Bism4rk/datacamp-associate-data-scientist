# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

'''
O código acima demonstra como importar um arquivo CSV para um DataFrame do pandas. Primeiro, a biblioteca pandas é importada com o alias 'pd'. Em seguida, o arquivo 'cars.csv' é lido usando a função `pd.read_csv()` e armazenado na variável `cars`, que é um DataFrame. Finalmente, o conteúdo do DataFrame `cars` é impresso na tela, exibindo os dados contidos no arquivo CSV.
'''