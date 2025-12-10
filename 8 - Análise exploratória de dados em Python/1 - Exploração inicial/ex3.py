import pandas as pd

# Import the required visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data=unemployment, x='2021', binwidth=1)
plt.show()

'''
O código acima cria um histograma da taxa de desemprego em 2021 utilizando a biblioteca seaborn para visualização. Ele importa as bibliotecas necessárias, carrega os dados do arquivo 'clean_unemployment.csv' e utiliza a função histplot() para gerar o histograma, definindo uma largura de bin de 1 para mostrar uma porcentagem completa em cada bin. Finalmente, o gráfico é exibido com plt.show().
'''