import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\food_consumption.csv', index_col=0)

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

print(emissions_by_country)

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)] 
print(outliers)

'''
O código acima demonstra como identificar outliers nas emissões totais de CO2 por país usando o intervalo interquartil (IQR). Primeiro, ele calcula as emissões totais de CO2 para cada país agrupando os dados. Em seguida, calcula o primeiro e o terceiro quartis, bem como o IQR. Com esses valores, define os limites inferior e superior para detectar outliers. Finalmente, filtra os países cujas emissões totais de CO2 estão fora desses limites e imprime esses outliers.
'''