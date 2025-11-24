import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\climate_change.csv', parse_dates=['date'], index_col='date')

fig, ax = plt.subplots()

# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)


# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time (years)', 'CO2 levels')

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', 'Time (years)', 'Relative temp (Celsius)')

# Annotate point with relative temperature >1 degree
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={'arrowstyle' : '->', 'color': 'gray'}) # type: ignore

plt.show()

'''
O código acima melhora a visualização de séries temporais ao não só anotar um ponto específico onde a temperatura relativa excedeu 1 grau Celsius, mas também usar uma seta para destacar esse ponto no gráfico. A função `plot_timeseries` é reutilizada para plotar tanto os níveis de CO2 quanto a temperatura relativa em eixos y separados, facilitando a comparação visual entre as duas variáveis ao longo do tempo. A anotação com seta ajuda a chamar a atenção para o evento significativo, tornando o gráfico mais informativo e fácil de interpretar.
'''