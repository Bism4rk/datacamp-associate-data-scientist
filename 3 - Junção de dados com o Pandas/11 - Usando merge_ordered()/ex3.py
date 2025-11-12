import pandas as pd

gdp = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\gdp2.csv')
pop = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\pop.csv')

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'], fill_method='ffill')

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'], fill_method='ffill')


# Print date_ctry
print(date_ctry)

'''
O código acima demonstra o uso da função merge_ordered() do Pandas para combinar dois DataFrames, gdp e pop, com base nas colunas 'date' e 'country'. A fusão é realizada duas vezes: primeiro com a ordem das colunas como ['date', 'country'] e depois como ['country', 'date'], utilizando o método de preenchimento 'ffill' para lidar com valores ausentes. Os DataFrames resultantes, ctry_date e date_ctry, são impressos para mostrar como a ordem das colunas afeta o resultado da fusão. No primeiro, observa-se que as linhas 2 e 3 apresentam diferenças devido à ordem das colunas na fusão.
'''