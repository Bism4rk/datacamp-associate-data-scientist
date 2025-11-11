import pandas as pd

non_mus_tcks = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\8 - Joins de filtragem\\non_mus_tcks.csv')
top_invoices = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\8 - Joins de filtragem\\top_invoices.csv')
genres = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\8 - Joins de filtragem\\genres.csv')

# Merge the non_mus_tcks and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))

'''
O código acima demonstra como identificar os gêneros musicais mais populares entre as faixas que geraram as maiores receitas. Primeiro, os DataFrames 'non_mus_tcks' e 'top_invoices' são mesclados com base na coluna 'tid' para obter as faixas associadas às faturas principais. Em seguida, o DataFrame 'non_mus_tcks' é filtrado para incluir apenas as faixas presentes no DataFrame resultante da mesclagem. Depois, essas faixas são agrupadas por 'gid' (identificador de gênero) e o número de faixas ('tid') em cada gênero é contado. Finalmente, o DataFrame resultante é mesclado com o DataFrame 'genres' para adicionar informações sobre os gêneros musicais, e o resultado é impresso.
'''