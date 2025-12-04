# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            linestyle='none', 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de pontos usando Seaborn e como rotacionar os rótulos do eixo x para melhor legibilidade. Primeiro, importamos as bibliotecas necessárias e carregamos o conjunto de dados 'mpg'. Em seguida, criamos um gráfico de pontos que mostra a aceleração média dos carros agrupados pela origem. Finalmente, rotacionamos os rótulos do eixo x em 90 graus para evitar sobreposição e melhorar a clareza da visualização antes de exibi-la.
'''