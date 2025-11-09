import pandas as pd

movies = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\movies.csv')
financials = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\financials.csv')

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

'''
O código acima demonstra como realizar uma junção à esquerda (left join) entre dois DataFrames usando a biblioteca Pandas em Python. A junção é feita com base na coluna 'id', que é comum a ambos os DataFrames: 'movies' e 'financials'. Após a junção, o código conta o número de valores ausentes na coluna 'budget' do DataFrame resultante 'movies_financials' e imprime esse número. Isso é útil para identificar quantos filmes não possuem informações financeiras associadas.
'''