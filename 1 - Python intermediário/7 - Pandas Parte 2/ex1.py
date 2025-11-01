# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)
# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

'''
O código acima demonstra como selecionar colunas específicas de um DataFrame do Pandas. Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV chamado 'cars.csv', definindo a primeira coluna como índice. Em seguida, ele imprime a coluna 'country' como uma Série do Pandas, depois como um DataFrame, e finalmente imprime um DataFrame contendo as colunas 'country' e 'drives_right'.
'''