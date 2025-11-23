import matplotlib.pyplot as plt
import pandas as pd
from ex2 import plot_timeseries

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

climate_change = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\climate_change.csv', parse_dates=['date'], index_col='date')

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change['co2'], "blue", 'Time (years)', 'CO2 levels')

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], "red", 'Time (years)', 'Relative temperature (Celsius)')

plt.show()

'''
O código acima demonstra como utilizar a função `plot_timeseries` definida em outro arquivo para criar um gráfico de séries temporais com duas variáveis diferentes. A variável 'co2' é plotada em azul no eixo y esquerdo, enquanto a variável 'relative_temp' é plotada em vermelho no eixo y direito. A função `twinx()` é utilizada para criar um segundo eixo y que compartilha o mesmo eixo x, permitindo a visualização simultânea de ambas as variáveis ao longo do tempo, com estilos visuais consistentes e personalizados.
'''