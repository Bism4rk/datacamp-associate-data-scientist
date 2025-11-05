import pandas as pd

avocados = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\11 - Visualização de dados\\avoplotto.pkl')

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()

'''
O código acima demonstra como criar um gráfico de barras usando o Pandas e Matplotlib para visualizar o número total de abacates vendidos por tamanho. Primeiro, os dados são carregados a partir de um arquivo pickle e as primeiras linhas são exibidas para inspeção. Em seguida, os dados são agrupados pelo tamanho do abacate e o total vendido é calculado. Finalmente, um gráfico de barras é gerado para representar visualmente esses totais, e o gráfico é exibido na tela.
'''