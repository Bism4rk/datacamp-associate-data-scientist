import matplotlib.pyplot as plt
import pandas as pd

summer_2016_medals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\summer2016.csv')

fig, ax = plt.subplots()

# Extract the "Sport" column
sports_column = summer_2016_medals['Sport']

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)

'''
O código acima demonstra como carregar um conjunto de dados de medalhas olímpicas de um arquivo CSV e extrair a coluna "Sport" para identificar os esportes únicos presentes no conjunto de dados. Utilizando a biblioteca Pandas, o código lê os dados, extrai a coluna relevante e utiliza o método `unique()` para obter uma lista dos esportes distintos, que são então impressos no console. Isso é útil para entender a variedade de esportes representados nos dados antes de prosseguir com análises ou visualizações adicionais.
'''