# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\seattle_weather_consolidated.csv')
austin_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\austin_weather_fixed.csv')

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

'''
O código acima demonstra como criar múltiplos gráficos (subplots) usando Matplotlib para visualizar dados climáticos de Seattle e Austin. Cada subplot exibe diferentes aspectos dos dados meteorológicos, como precipitação e temperatura média mensal, organizados em uma grade de 2x2.
'''