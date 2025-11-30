# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", data=mpg, kind='scatter', size='cylinders')

# Show plot
plt.show()

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders", hue='cylinders')

# Show plot
plt.show()

'''
O código acima demonstra como criar gráficos de dispersão usando a biblioteca Seaborn em Python. Primeiro, um gráfico de dispersão é criado para visualizar a relação entre a potência (horsepower) e o consumo de combustível (mpg) dos veículos, com o tamanho dos pontos representando o número de cilindros (cylinders). Em seguida, o gráfico é aprimorado ao adicionar uma dimensão adicional: a cor dos pontos também representa o número de cilindros, permitindo uma visualização mais rica dos dados. Cada etapa do processo é seguida pela exibição do gráfico resultante.
'''