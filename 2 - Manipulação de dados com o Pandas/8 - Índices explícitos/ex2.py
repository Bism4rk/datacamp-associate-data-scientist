import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')
temperatures_ind = temperatures.set_index('city')


# Make a list of cities to subset on
cities = ["London", "Paris"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

'''
O código acima demonstra duas maneiras de fazer um subconjunto de um DataFrame do Pandas com base em uma lista de cidades. Primeiro, ele cria uma lista chamada 'cities' contendo os nomes das cidades "London" e "Paris". Em seguida, ele mostra como fazer o subconjunto do DataFrame original 'temperatures' usando colchetes e o método 'isin()' para filtrar as linhas onde a coluna 'city' corresponde às cidades na lista. Depois, o código faz o mesmo subconjunto no DataFrame 'temperatures_ind', que tem a coluna 'city' definida como índice, utilizando o método '.loc[]' para acessar diretamente as linhas correspondentes às cidades na lista.
'''