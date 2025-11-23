import matplotlib.pyplot as plt
import pandas as pd

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

climate_change = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\climate_change.csv', parse_dates=['date'], index_col='date')

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()

'''
O código acima demonstra como criar um gráfico de série temporal usando Matplotlib para visualizar os níveis de CO2 durante a década de 1970. A variável 'seventies' filtra os dados do DataFrame para o período especificado, e o gráfico resultante exibe a variação dos níveis de CO2 ao longo desses anos.
'''