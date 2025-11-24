import matplotlib.pyplot as plt
import pandas as pd

medals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\medals_by_country_2016.csv', index_col=0)

fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals['Gold'])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel('Number of medals')

plt.show()

'''
O código acima demonstra como criar um gráfico de barras para visualizar o número de medalhas de ouro conquistadas por diferentes países nas Olimpíadas de 2016. Utilizando a biblioteca Matplotlib, o gráfico apresenta as medalhas no eixo y e os países no eixo x, com os nomes dos países rotacionados em 90 graus para melhor legibilidade. A visualização facilita a comparação quantitativa entre os países em termos de desempenho olímpico.
'''