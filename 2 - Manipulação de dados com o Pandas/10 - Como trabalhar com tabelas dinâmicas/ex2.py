import pandas as pd
from ex1 import temp_by_country_city_vs_year

# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi')]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi'), 2005:2010]

'''
O código acima demonstra como realizar subsetting em um DataFrame do Pandas com índices hierárquicos (MultiIndex). Utilizando o método .loc[], é possível selecionar linhas e colunas específicas com base nos níveis do índice. No exemplo, o DataFrame 'temp_by_country_city_vs_year' contém dados de temperatura organizados por país e cidade (níveis do índice) e anos (colunas). O código mostra três exemplos de subsetting:
1. Seleção de todas as cidades entre os países Egito e Índia.
2. Seleção de cidades específicas, de Cairo (Egito) a Delhi (Índia).
3. Seleção de cidades específicas entre Egito e Índia, limitando os dados aos anos de 2005 a 2010.

'''