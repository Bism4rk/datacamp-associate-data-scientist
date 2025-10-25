# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

'''
O código acima demonstra como selecionar linhas específicas de um DataFrame do Pandas usando indexação por fatias (slicing). Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV chamado 'cars.csv', definindo a primeira coluna como índice. Em seguida, ele imprime as três primeiras observações (linhas) do DataFrame e, em seguida, imprime a quarta, quinta e sexta observação.
'''