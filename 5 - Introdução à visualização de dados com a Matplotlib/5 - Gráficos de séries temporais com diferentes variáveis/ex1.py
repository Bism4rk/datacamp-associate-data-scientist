import matplotlib.pyplot as plt
import pandas as pd

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

climate_change = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\climate_change.csv', parse_dates=['date'], index_col='date')

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change['co2'], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change['relative_temp'], color='red')

plt.show()

'''
O código acima demonstra como criar um gráfico de séries temporais com duas variáveis diferentes usando Matplotlib. A variável 'co2' é plotada em azul no eixo y esquerdo, enquanto a variável 'relative_temp' é plotada em vermelho no eixo y direito. A função `twinx()` é utilizada para criar um segundo eixo y que compartilha o mesmo eixo x, permitindo a visualização simultânea de ambas as variáveis ao longo do tempo.
'''