# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\seattle_weather.csv')
austin_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\austin_weather.csv')

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

print(seattle_weather.head())
print(austin_weather.head())

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["DATE"], seattle_weather['MLY-PRCP-NORMAL'])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["DATE"], austin_weather['MLY-PRCP-NORMAL'])

# Call the show function
plt.show()

'''
O código acima demonstra como criar um gráfico de linhas com múltiplas séries temporais usando Matplotlib. Ele plota os valores de precipitação normal mensal para Seattle e Austin em um único gráfico, permitindo a comparação visual entre as duas cidades ao longo dos meses do ano.
'''