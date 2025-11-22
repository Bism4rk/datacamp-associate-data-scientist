# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\seattle_weather_consolidated.csv')
austin_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\austin_weather_fixed.csv')

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["MLY-PRCP-NORMAL"], seattle_weather["MLY-PRCP-NORMAL"], color = "b")
ax[0].plot(seattle_weather["MLY-PRCP-NORMAL"], seattle_weather["MLY-PRCP-25PCTL"], color = "b", linestyle = "--")
ax[0].plot(seattle_weather["MLY-PRCP-NORMAL"], seattle_weather["MLY-PRCP-75PCTL"], color = "b", linestyle = "--")

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather["MLY-PRCP-NORMAL"], austin_weather["MLY-PRCP-NORMAL"], color = "r")
ax[1].plot(austin_weather["MLY-PRCP-NORMAL"], austin_weather["MLY-PRCP-25PCTL"], color = "r", linestyle = "--")
ax[1].plot(austin_weather["MLY-PRCP-NORMAL"], austin_weather["MLY-PRCP-75PCTL"], color = "r", linestyle = "--")

plt.show()

'''
O código acima demonstra como criar múltiplos gráficos (subplots) usando Matplotlib para comparar dados de precipitação de Seattle e Austin. Cada subplot exibe a precipitação normal, bem como os percentis 25 e 75, permitindo uma análise visual das variações climáticas entre as duas cidades.
'''