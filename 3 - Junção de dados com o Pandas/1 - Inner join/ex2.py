import pandas as pd

taxi_owners = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\taxi_owners.csv')
taxi_veh = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\taxi_vehicles.csv')

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

'''
O código acima demonstra como realizar uma junção interna (inner join) entre dois DataFrames do Pandas, 'taxi_owners' e 'taxi_vehicles', com base na coluna comum 'vid'. A função merge é utilizada para combinar os dados, e o parâmetro suffixes é especificado para diferenciar colunas com nomes idênticos provenientes dos dois DataFrames. Após a junção, o código calcula e imprime a contagem de valores únicos na coluna 'fuel_type', permitindo identificar o tipo de combustível mais popular entre os veículos de táxi.
'''