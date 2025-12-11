import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Print the mean and standard deviation of rates for 2019 and 2020 
print(unemployment[["2019", "2020"]].agg(['mean', 'std']))

# Print mean and standard deviation grouped by continent
print(unemployment[["continent", "2019", "2020"]].groupby('continent').agg(['mean', 'std']))

'''
O código acima demonstra como calcular estatísticas descritivas básicas, como média e desvio padrão, tanto para o conjunto de dados geral quanto agrupado por uma categoria específica (neste caso, continente). Isso é útil para entender a distribuição dos dados e identificar possíveis variações entre diferentes grupos.
'''