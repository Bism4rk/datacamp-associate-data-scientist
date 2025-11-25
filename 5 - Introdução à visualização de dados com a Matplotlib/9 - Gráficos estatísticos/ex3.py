import matplotlib.pyplot as plt
import pandas as pd

mens_gymnastics = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\mens_gymnastics.csv')
mens_rowing = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\mens_rowing.csv')

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])

# Add x-axis tick labels:
ax.set_xticklabels(['Rowing', 'Gymnastics'])

# Add a y-axis label
ax.set_ylabel('Height (cm)')

plt.show()

'''
O códgio acima demonstra como criar um gráfico de caixa (boxplot) para comparar a distribuição das alturas entre dois grupos diferentes: ginastas masculinos e remadores masculinos. Utilizando a biblioteca Matplotlib, o código lê os dados de arquivos CSV, plota boxplots para cada grupo e rotula os eixos para melhor compreensão. Isso permite uma análise visual eficaz das diferenças na distribuição das alturas entre os dois esportes.
'''