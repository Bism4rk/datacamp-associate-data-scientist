# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\seattle_weather_consolidated.csv')
austin_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\austin_weather_fixed.csv')

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()


ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel('Time (months)')

# Customize the y-axis label
ax.set_ylabel('Precipitation (inches)')

# Add the title
ax.set_title('Weather patterns in Austin and Seattle')

# Display the figure
plt.show()


'''
O código acima demonstra como personalizar um gráfico de linhas usando Matplotlib. Primeiro, os dados de precipitação mensal normal para Seattle e Austin são carregados a partir de arquivos CSV. Em seguida, uma figura e um conjunto de eixos são criados com plt.subplots(). As linhas de precipitação para ambas as cidades são plotadas no mesmo gráfico. As personalizações incluem a adição de rótulos aos eixos x e y, bem como um título ao gráfico. Finalmente, o gráfico é exibido com plt.show().
'''