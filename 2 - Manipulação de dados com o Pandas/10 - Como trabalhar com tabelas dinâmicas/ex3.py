import pandas as pd
from ex2 import temp_by_country_city_vs_year

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])

'''
O código acima calcula a temperatura média mundial por ano e identifica o ano com a maior temperatura média. Em seguida, calcula a temperatura média por cidade e identifica a cidade com a menor temperatura média. Os resultados são impressos, mostrando o ano mais quente e a cidade mais fria com base nos dados fornecidos na tabela dinâmica importada de ex2.py.
'''