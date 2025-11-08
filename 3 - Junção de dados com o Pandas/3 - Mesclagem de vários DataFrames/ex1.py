import pandas as pd

cal = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\cta_calendar.csv')
ridership = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\cta_ridership.csv')
stations = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\stations.pkl')

# Not part of exercise, added because VS Code keeps freaking out about type mismatch during merge
ridership['station_id'] = ridership['station_id'].astype(str)
stations['station_id'] = stations['station_id'].astype(str)

# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal, on=['year', 'month', 'day'])

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']).merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

'''
O código acima demonstra como mesclar vários DataFrames usando o Pandas e filtrar os dados resultantes com base em critérios específicos. Primeiro, ele lê três conjuntos de dados: um calendário, dados de passageiros e informações sobre estações. Em seguida, ele mescla os DataFrames de passageiros e calendário com base nas colunas 'year', 'month' e 'day'. Depois, ele mescla o DataFrame resultante com o DataFrame de estações usando a coluna 'station_id'. Finalmente, o código cria um filtro para selecionar os dados de julho, dias úteis e a estação 'Wilson', e calcula a soma total de passageiros para esses critérios, exibindo o resultado.
'''