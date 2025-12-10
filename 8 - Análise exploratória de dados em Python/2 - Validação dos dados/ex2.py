import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment['continent'].isin(['Oceania'])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])

'''
O código acima demonstra como filtrar um DataFrame do pandas para excluir registros relacionados a países na Oceania. Ele cria uma Series booleana que identifica quais continentes não são Oceania usando o método isin() e o operador de negação (~). Em seguida, utiliza essa Series para filtrar o DataFrame original, imprimindo apenas os registros que não pertencem à Oceania.
'''