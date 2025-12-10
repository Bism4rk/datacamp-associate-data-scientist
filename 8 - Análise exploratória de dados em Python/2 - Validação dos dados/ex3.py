import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Print the minimum and maximum unemployment rates during 2021
print(unemployment['2021'].min(), unemployment['2021'].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(data=unemployment, x='2021', y='continent')
plt.show()

'''
O código acima demonstra como visualizar a distribuição das taxas de desemprego em 2021, segmentadas por continente, utilizando um boxplot. Ele importa as bibliotecas pandas, matplotlib.pyplot e seaborn, carrega os dados do arquivo 'clean_unemployment.csv', imprime os valores mínimo e máximo das taxas de desemprego em 2021 e cria um boxplot para ilustrar a variação das taxas de desemprego entre os diferentes continentes.
'''