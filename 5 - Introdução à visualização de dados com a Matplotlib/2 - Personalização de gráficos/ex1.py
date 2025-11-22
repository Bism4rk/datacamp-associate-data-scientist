# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\seattle_weather.csv')
austin_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\austin_weather.csv')

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

print(seattle_weather)

# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"], color='b', marker='o', linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"], color='r', marker='v', linestyle='--')

# Call show to display the resulting plot
plt.show()

'''
O código acima demonstra como personalizar gráficos em Matplotlib, incluindo a escolha de cores, marcadores e estilos de linha para diferentes conjuntos de dados. No exemplo, os dados de precipitação normal mensal de Seattle e Austin são plotados em um único gráfico, com cada cidade representada por uma cor e estilo distintos. A função plt.subplots() é usada para criar uma figura e um conjunto de eixos, permitindo a personalização detalhada dos gráficos. Finalmente, plt.show() exibe o gráfico resultante.
'''