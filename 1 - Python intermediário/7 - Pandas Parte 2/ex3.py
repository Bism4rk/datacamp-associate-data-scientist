# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)
# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

'''
O código acima demonstra como selecionar linhas específicas de um DataFrame do Pandas usando os métodos iloc e loc. Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV chamado 'cars.csv', definindo a primeira coluna como índice. Em seguida, ele imprime a observação (linha) correspondente ao Japão usando iloc, que seleciona por posição inteira, e depois imprime as observações para Austrália e Egito usando loc, que seleciona por rótulo de índice.
'''