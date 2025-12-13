import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')

# Plot a histogram of flight prices
sns.histplot(data=planes, x="Price")
plt.show()

# Display descriptive statistics for flight duration
print(planes['Duration'].describe())

'''
O código acima demonstra como carregar um conjunto de dados de voos a partir de um arquivo CSV e realizar uma análise exploratória inicial. Primeiro, ele importa as bibliotecas necessárias: pandas para manipulação de dados, matplotlib.pyplot e seaborn para visualização de dados, e numpy para operações numéricas. Em seguida, o código lê os dados do arquivo 'planes.csv' e os armazena em um DataFrame chamado 'planes'. Depois, ele cria um histograma dos preços dos voos usando a função histplot do seaborn, o que ajuda a visualizar a distribuição dos preços. Finalmente, o código exibe estatísticas descritivas da duração dos voos, como média, mediana, desvio padrão, valores mínimos e máximos, utilizando o método describe() do pandas. Essa análise inicial é fundamental para entender a estrutura dos dados e identificar possíveis valores discrepantes ou padrões interessantes.
'''

