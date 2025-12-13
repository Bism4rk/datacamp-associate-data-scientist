import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

# Subset the data
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]

print(planes["Price"].describe())

'''
O código acima demonstra como identificar e tratar valores discrepantes (outliers) em um conjunto de dados de voos, especificamente na coluna de preços. Primeiro, ele calcula o 75º e o 25º percentil dos preços dos voos usando o método quantile() do pandas. Em seguida, calcula o intervalo interquartil (IQR) subtraindo o 25º percentil do 75º percentil. Com o IQR, o código determina os limites superior e inferior para identificar valores discrepantes, aplicando a regra de 1,5 vezes o IQR. Finalmente, o código filtra o DataFrame 'planes' para manter apenas os registros cujos preços estão dentro desses limites, efetivamente removendo os outliers. Por fim, ele exibe as estatísticas descritivas atualizadas da coluna de preços após a remoção dos valores discrepantes. Essa abordagem é essencial para garantir que a análise subsequente dos dados não seja distorcida por valores extremos.
'''