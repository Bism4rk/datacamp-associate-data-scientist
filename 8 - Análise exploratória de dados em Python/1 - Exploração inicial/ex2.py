import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Count the values associated with each continent in unemployment
print(unemployment.value_counts('continent'))

'''
O código acima realiza uma contagem dos valores associados a cada continente na coluna 'continent' do DataFrame de desemprego. Ele importa a biblioteca pandas, carrega os dados do arquivo 'clean_unemployment.csv' e utiliza o método value_counts() para contar as ocorrências de cada continente, imprimindo o resultado.
'''