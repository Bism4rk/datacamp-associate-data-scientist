# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)

# Print out drives_right value of Morocco
print(cars.loc[['MOR'], 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

'''
O código acima demonstra como selecionar valores específicos e sub-DataFrames de um DataFrame do Pandas usando o método loc. Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV chamado 'cars.csv', definindo a primeira coluna como índice. Em seguida, ele imprime o valor da coluna 'drives_right' para o Marrocos. Depois, ele imprime um sub-DataFrame contendo as colunas 'country' e 'drives_right' para a Rússia e o Marrocos.
'''