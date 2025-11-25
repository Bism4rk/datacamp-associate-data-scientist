import matplotlib.pyplot as plt
import pandas as pd

mens_gymnastics = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\mens_gymnastics.csv')
mens_rowing = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\mens_rowing.csv')

fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing['Height'].mean(), yerr=mens_rowing['Height'].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics['Height'].mean(), yerr=mens_gymnastics['Height'].std())

# Label the y-axis
ax.set_ylabel('Height (cm)')

plt.show()

'''
O código acima demonstra como criar um gráfico de barras para comparar a média e o desvio padrão da altura entre dois grupos diferentes: ginastas masculinos e remadores masculinos. Utilizando a biblioteca Matplotlib, o código lê os dados de arquivos CSV, plota barras com barras de erro para cada grupo e rotula os eixos para melhor compreensão. Isso permite uma análise visual eficaz das diferenças na altura entre os dois esportes.
'''