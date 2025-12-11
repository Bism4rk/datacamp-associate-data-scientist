import pandas as pd

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')

# Count the number of missing values in each column
print(planes.isna().sum())

# Find the five percent threshold
threshold = len(planes) * 0.05

# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())

'''
O código acima demonstra como lidar com dados faltantes em um DataFrame do Pandas. Primeiro, ele conta o número de valores ausentes em cada coluna. Em seguida, calcula um limite de cinco por cento do total de linhas para determinar quais colunas têm uma quantidade aceitável de dados faltantes. Finalmente, ele remove as linhas que contêm valores ausentes nessas colunas selecionadas, ajudando a limpar o conjunto de dados para análises futuras.
'''