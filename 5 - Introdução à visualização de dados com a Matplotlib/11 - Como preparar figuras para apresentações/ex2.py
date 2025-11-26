# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\seattle_weather_consolidated.csv')
austin_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\austin_weather_fixed.csv')

# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

plt.show()


# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()

ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])

plt.show()

'''
O código acima demonstra como alterar o estilo de gráficos no Matplotlib usando estilos predefinidos. Primeiro, o estilo "ggplot" é aplicado para criar um gráfico de linhas que mostra a temperatura média mensal em Seattle. Em seguida, o estilo "Solarize_Light2" é aplicado para criar outro gráfico de linhas que exibe a temperatura média mensal em Austin. Cada gráfico é exibido separadamente, ilustrando como diferentes estilos podem afetar a aparência visual dos gráficos gerados.
'''