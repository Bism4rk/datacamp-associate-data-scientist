from ex1 import homelessness

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

'''
O código acima demonstra como acessar diferentes componentes de um DataFrame do Pandas. Especificamente, ele imprime os valores contidos no DataFrame, os nomes das colunas e os índices das linhas. O atributo values retorna uma matriz numpy com os dados do DataFrame, columns fornece um índice dos nomes das colunas, e index retorna o índice das linhas, que pode ser útil para identificar ou acessar linhas específicas.
'''