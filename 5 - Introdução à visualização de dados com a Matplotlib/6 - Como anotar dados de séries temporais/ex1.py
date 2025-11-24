import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\climate_change.csv', parse_dates=['date'], index_col='date')

fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1)) # type: ignore

plt.show()

'''
O código acima demonstra como anotar um ponto específico em um gráfico de séries temporais usando Matplotlib. Ele lê um conjunto de dados sobre mudanças climáticas, plota a série temporal de temperaturas relativas e adiciona uma anotação no ponto onde a temperatura excedeu 1 grau Celsius. A anotação é feita utilizando o método `annotate`, que permite destacar informações importantes diretamente no gráfico, facilitando a interpretação dos dados visualizados.
'''