import pandas as pd

tracks_master = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\9 - Concatenar DataFrames verticalmente\\tracks_master.csv')
tracks_ride = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\9 - Concatenar DataFrames verticalmente\\tracks_ride.csv')
tracks_st = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\9 - Concatenar DataFrames verticalmente\\tracks_st.csv')

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], ignore_index=True, sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], join="inner", sort=True)
print(tracks_from_albums)

'''
O código acima demonstra como concatenar três DataFrames do Pandas verticalmente, utilizando diferentes opções para controlar o índice e as colunas incluídas no resultado final. Primeiro, os DataFrames são concatenados mantendo os índices originais. Em seguida, o índice é redefinido para que vá de 0 a n-1. Por fim, apenas as colunas comuns a todos os DataFrames são mantidas na concatenação final. 
'''

