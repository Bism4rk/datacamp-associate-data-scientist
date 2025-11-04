import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])

'''
O código acima demonstra o uso do método iloc do Pandas para acessar e fatiar dados em um DataFrame com base em índices inteiros. Primeiro, ele recupera o valor específico localizado na 23ª linha e 2ª coluna (índices 22 e 1). Em seguida, o código utiliza fatiamento para obter as primeiras cinco linhas do DataFrame completo. Depois, ele fatiar todas as linhas, mas apenas as colunas 3 e 4 (índices 2 e 3). Finalmente, o código combina ambos os tipos de fatiamento para obter as primeiras cinco linhas, mas apenas das colunas 3 e 4.
'''