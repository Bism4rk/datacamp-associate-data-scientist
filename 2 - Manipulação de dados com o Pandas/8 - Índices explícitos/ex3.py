import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

'''
O código acima demonstra como fazer um subconjunto de um DataFrame do Pandas que possui um índice hierárquico (multi-índice). Primeiro, ele lê um conjunto de dados de temperaturas e define um índice composto pelas colunas 'country' e 'city'. Em seguida, ele cria uma lista de tuplas chamada 'rows_to_keep', que contém os pares de país e cidade que se deseja manter no subconjunto. Finalmente, o código utiliza o método '.loc[]' para acessar diretamente as linhas correspondentes às tuplas na lista 'rows_to_keep', exibindo o subconjunto resultante do DataFrame.
'''