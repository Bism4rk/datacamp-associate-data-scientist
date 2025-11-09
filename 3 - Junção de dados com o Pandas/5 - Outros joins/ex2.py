import pandas as pd
import matplotlib.pyplot as plt

movie_to_genres = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\movie_to_genres.csv')
movies = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\movies.csv')

pop_movies = movies.sort_values('popularity', ascending=False).head(10)
print(pop_movies)

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on='movie_id', 
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

'''
O código acima demonstra como realizar uma junção à direita (right join) entre dois DataFrames usando a biblioteca Pandas em Python. Primeiro, ele seleciona os 10 filmes mais populares do DataFrame 'movies'. Em seguida, realiza uma junção à direita entre o DataFrame 'movie_to_genres' e o subconjunto dos filmes populares, com base nas colunas 'movie_id' e 'id'. Depois, o código agrupa os dados resultantes pelo gênero e conta o número de filmes em cada gênero. Finalmente, ele plota um gráfico de barras para visualizar a contagem de gêneros entre os filmes mais populares.
'''