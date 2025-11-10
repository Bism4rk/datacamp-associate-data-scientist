import pandas as pd

sequels = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\sequels_cleaned.csv', index_col='id')
financials = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\financials_cleaned.csv', index_col='id')

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())

'''
O código acima demonstra como mesclar dois DataFrames do Pandas usando índices e colunas específicas. Primeiro, os dados de sequências e financeiros são carregados a partir de arquivos CSV, com a coluna 'id' definida como índice. Em seguida, os DataFrames são mesclados com base no índice 'id' utilizando uma junção à esquerda (left join). Depois, é realizada uma auto-mesclagem (self merge) para comparar filmes originais com suas sequências, utilizando colunas específicas para a junção. Uma nova coluna 'diff' é criada para calcular a diferença de receita entre as sequências e os filmes originais. Finalmente, as primeiras linhas do DataFrame resultante, ordenadas pela diferença de receita, são exibidas para análise.
'''