# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style="origin", hue='origin')

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de dispersão usando a biblioteca Seaborn em Python. Ele importa as bibliotecas necessárias, lê um conjunto de dados sobre carros (mpg.csv) e cria um gráfico de dispersão que mostra a relação entre a aceleração e o consumo de combustível (mpg). As variáveis "origin" são usadas para diferenciar os pontos no gráfico por estilo e cor, facilitando a visualização das categorias de origem dos carros. Finalmente, o gráfico é exibido usando plt.show().
'''