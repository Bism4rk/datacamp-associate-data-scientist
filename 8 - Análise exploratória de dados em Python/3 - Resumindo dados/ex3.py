import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Create a bar plot of continents and their average unemployment
sns.barplot(data=unemployment, x='continent', y='2021')
plt.show()

'''
O código acima demonstra como visualizar dados resumidos usando um gráfico de barras para comparar as médias das taxas de desemprego por continente em 2021. A visualização ajuda a identificar rapidamente diferenças entre os continentes - as barras mais altas indicam taxas de desemprego médias mais elevadas, e o intervalo de confiança (a linha fina sobre cada barra) fornece uma indicação da incerteza em torno dessas médias.
'''