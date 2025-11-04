import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

'''
O código acima demonstra como manipular índices em um DataFrame do Pandas. Primeiro, ele lê um conjunto de dados de temperaturas e exibe o DataFrame original. Em seguida, ele define a coluna 'city' como o índice do DataFrame, criando um novo DataFrame chamado temperatures_ind, que também é exibido. Depois, o código mostra como redefinir o índice do DataFrame mantendo os dados da coluna 'city' como uma coluna normal. Finalmente, ele redefine o índice novamente, mas desta vez descarta a coluna 'city', resultando em um DataFrame com um índice padrão numérico.
'''