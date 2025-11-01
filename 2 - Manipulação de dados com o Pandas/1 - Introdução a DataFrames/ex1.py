import pandas as pd

homelessness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\2 - Classificação e criação de subconjuntos\\homelessness.csv') # actually works now

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

'''
O código demonstra como obter informações básicas sobre um DataFrame do Pandas, incluindo as primeiras linhas, informações gerais, dimensões e estatísticas descritivas. O DataFrame utilizado contém dados sobre pessoas em situação de rua nos Estados Unidos. O método head() exibe as primeiras cinco linhas, info() fornece um resumo conciso do DataFrame, shape retorna uma tupla com o número de linhas e colunas, e describe() gera estatísticas descritivas para colunas numéricas.
'''
