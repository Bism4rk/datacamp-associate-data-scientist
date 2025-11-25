# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\seattle_weather_consolidated.csv')
austin_weather = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\austin_weather_fixed.csv')

fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'], yerr=seattle_weather['MLY-TAVG-STDDEV'])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'], yerr=austin_weather['MLY-TAVG-STDDEV']) 

# Set the y-axis label
ax.set_ylabel('Temperature (Fahrenheit)')

plt.show()

'''
O código acima demonstra como criar um gráfico de linhas com barras de erro usando o Matplotlib. Primeiro, os dados de temperatura média mensal e o desvio padrão para Seattle e Austin são carregados a partir de arquivos CSV. Em seguida, um gráfico é criado com barras de erro que representam a variabilidade das temperaturas médias mensais em cada cidade. O eixo y é rotulado como "Temperature (Fahrenheit)" para indicar a unidade de medida das temperaturas exibidas no gráfico.
'''