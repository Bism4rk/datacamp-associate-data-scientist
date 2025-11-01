# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)

# Print out drives_right column as Series
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:, [0,2]])

'''
O código acima demonstra como selecionar colunas específicas de um DataFrame do Pandas usando indexação baseada em posições. Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV chamado 'cars.csv', definindo a primeira coluna como índice. Em seguida, ele imprime a terceira coluna ('drives_right') como uma Série do Pandas, depois como um DataFrame, e finalmente imprime um DataFrame contendo as colunas 'cars_per_cap' e 'drives_right'.
'''