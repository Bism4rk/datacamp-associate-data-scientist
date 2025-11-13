import pandas as pd
import matplotlib.pyplot as plt

gdp = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\gdp2.csv')
pop = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\pop.csv')

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()

'''
O código acima demonstra o uso da função merge_ordered() do Pandas para combinar dois DataFrames, gdp e pop, com base nas colunas 'country' e 'date'. Após a fusão, uma nova coluna chamada 'gdp_per_capita' é adicionada ao DataFrame resultante, calculando o PIB per capita dividindo o PIB pela população. Em seguida, os dados são reorganizados usando a função pivot_table(), onde o índice é a data e as colunas são os países. Finalmente, os dados são filtrados para incluir apenas as datas iguais ou posteriores a 1991-01-01, e um gráfico é gerado para visualizar o PIB per capita recente ao longo do tempo para cada país.
'''