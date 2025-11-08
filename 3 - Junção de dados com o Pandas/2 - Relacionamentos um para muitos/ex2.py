import pandas as pd

licenses = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\licenses.csv')
biz_owners = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\business_owners.csv')

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in descending order
sorted_df = counted_df.sort_values(by='account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

'''
O código acima demonstra como realizar uma junção entre dois DataFrames usando o Pandas, seguida por uma agregação e ordenação dos dados resultantes. Primeiro, os dados de licenças e proprietários de negócios são carregados a partir de arquivos CSV. Em seguida, os DataFrames são mesclados com base na coluna 'account', criando um novo DataFrame que combina informações de ambos. Depois disso, os dados são agrupados pela coluna 'title', contando o número de contas associadas a cada título. Finalmente, o DataFrame resultante é ordenado em ordem decrescente com base na contagem de contas, e as primeiras linhas do DataFrame ordenado são exibidas. Isso é útil para identificar quais títulos têm o maior número de contas associadas.
'''