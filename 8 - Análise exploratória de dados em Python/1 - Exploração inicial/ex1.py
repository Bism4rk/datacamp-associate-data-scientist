import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Print the first five rows of unemployment
print(unemployment.head())

# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())

'''
O código acima realiza uma análise exploratória inicial dos dados de desemprego contidos no arquivo 'clean_unemployment.csv'. Ele importa as bibliotecas necessárias, carrega os dados em um DataFrame do pandas e imprime as primeiras cinco linhas, um resumo das informações do DataFrame e estatísticas descritivas para as colunas numéricas.
'''