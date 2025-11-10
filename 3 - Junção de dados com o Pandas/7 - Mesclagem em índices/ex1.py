import pandas as pd

movies = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\movies_cleaned.csv', index_col='id')
ratings = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\ratings_cleaned.csv', index_col='id')

print(movies.head())
print(ratings.head())

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, how='left', on='id')

# Print the first few rows of movies_ratings
print(movies_ratings.head())

'''
O código acima demonstra como mesclar dois DataFrames do Pandas usando um índice comum. Primeiro, os dados de filmes e avaliações são carregados a partir de arquivos CSV, com a coluna 'id' definida como índice. Em seguida, a função merge é utilizada para combinar os dois DataFrames com base no índice 'id', utilizando uma junção à esquerda (left join). Finalmente, as primeiras linhas do DataFrame resultante são exibidas para verificação.
'''