import pandas as pd

movie_to_genres = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\movie_to_genres.csv')
movies = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\movies.csv')

scifi_movies = movie_to_genres[movie_to_genres['genre'] == 'Science Fiction']
action_movies = movie_to_genres[movie_to_genres['genre'] == 'Action']

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, left_on="id", right_on="movie_id")

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

'''
O código acima demonstra como realizar uma junção à direita (right join) entre dois subconjuntos de um DataFrame usando a biblioteca Pandas em Python. Primeiro, ele filtra os filmes de ficção científica e ação a partir do DataFrame 'movie_to_genres'. Em seguida, realiza uma junção à direita entre esses dois subconjuntos com base na coluna 'movie_id'. Depois, seleciona apenas as linhas onde o gênero de ação é nulo, indicando filmes que são exclusivamente de ficção científica. Finalmente, o código faz uma junção interna (inner join) entre o DataFrame 'movies' e o subconjunto resultante para obter detalhes completos dos filmes de ficção científica, e imprime as primeiras linhas e a forma do DataFrame resultante.
'''