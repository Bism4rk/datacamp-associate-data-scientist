import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\climate_change.csv', parse_dates=['date'], index_col='date')

fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change['co2'], climate_change['relative_temp'])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel('CO2 (ppm)')

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel('Relative temperature (C)')

plt.show()

'''
O código acima demonstra como criar um gráfico de dispersão para comparar quantitativamente os níveis de CO2 com a temperatura relativa ao longo do tempo. Cada ponto no gráfico representa uma observação dos dados, permitindo visualizar a relação entre as duas variáveis. O eixo x mostra os níveis de CO2 em partes por milhão (ppm), enquanto o eixo y exibe a temperatura relativa em graus Celsius. Essa visualização é útil para identificar tendências ou correlações entre o aumento dos níveis de CO2 e as mudanças na temperatura relativa.
'''