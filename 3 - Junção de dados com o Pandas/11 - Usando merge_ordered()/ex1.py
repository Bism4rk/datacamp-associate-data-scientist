import pandas as pd

gdp = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\gdp.csv')
sp500 = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\sp500.csv')

# # Use merge_ordered() to merge gdp and sp500 on year and date
# gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', how='left')

# # Print gdp_sp500
# print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, and forward fill missing values
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())


'''
O código acima demonstra como usar a função merge_ordered() do Pandas para combinar dois DataFrames com base em colunas específicas, preenchendo valores ausentes com o método de preenchimento para frente (forward fill). Após a junção, ele extrai as colunas 'gdp' e 'returns' e calcula a correlação entre elas.
'''