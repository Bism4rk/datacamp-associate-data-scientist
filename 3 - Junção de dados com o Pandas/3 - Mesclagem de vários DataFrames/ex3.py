import pandas as pd

census = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\Chicago_census.csv')
land_use = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\land_use.csv')
licenses = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\licenses.csv')

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward').merge(licenses, on='ward', suffixes=('_cen', '_lic'))

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'], 
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

'''
O código acima demonstra como mesclar vários DataFrames usando o Pandas, aplicando sufixos para diferenciar colunas com nomes semelhantes. Primeiro, ele lê três conjuntos de dados: uso do solo, censo e licenças, todos relacionados a bairros (wards) em Chicago. Em seguida, ele mescla os DataFrames de uso do solo e censo com base na coluna 'ward', e depois mescla o resultado com o DataFrame de licenças, adicionando sufixos '_cen' e '_lic' para distinguir as colunas provenientes dos diferentes DataFrames. Após a mesclagem, o código agrupa os dados resultantes por 'ward', 'pop_2010' (população em 2010) e 'vacant' (imóveis vagos), contando o número de contas associadas a cada grupo. Finalmente, ele ordena os resultados com base na quantidade de imóveis vagos, número de contas e população, e imprime as primeiras linhas do DataFrame ordenado.
'''