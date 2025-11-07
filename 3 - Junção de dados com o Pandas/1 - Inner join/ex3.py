import pandas as pd

census = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\Chicago_census.csv')
wards = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\Chicago_wards.csv')

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head()) # type: ignore

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward') # type: ignore

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)

# Print the first few rows of the wards_altered table to view the change 
print(wards_altered[['ward']].head()) # type: ignore

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward') # type: ignore

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)

'''
O código acima demonstra como realizar junções internas (inner joins) entre DataFrames do Pandas, especificamente entre os DataFrames 'wards' e 'census'. Inicialmente, uma junção é feita diretamente entre esses dois DataFrames com base na coluna comum 'ward', e a forma (shape) do DataFrame resultante é impressa. Em seguida, o código ilustra o impacto de alterar os dados em um dos DataFrames antes da junção. Primeiro, o DataFrame 'census' é alterado (census_altered) e a junção é realizada novamente, mostrando como a forma do DataFrame resultante pode mudar. Depois, o DataFrame 'wards' é alterado (wards_altered) e a junção é feita novamente com o DataFrame original 'census', permitindo observar novamente as mudanças na forma do DataFrame resultante. Isso destaca a importância da integridade dos dados ao realizar junções entre conjuntos de dados.
'''

