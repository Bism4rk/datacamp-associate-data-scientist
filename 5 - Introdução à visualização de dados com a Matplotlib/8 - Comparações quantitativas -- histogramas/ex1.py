import matplotlib.pyplot as plt
import pandas as pd

mens_gymnastics = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\mens_gymnastics.csv')
mens_rowing = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\mens_rowing.csv')

fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel('Weight (kg)')

# Set the y-axis label to "# of observations"
ax.set_ylabel('# of observations')

plt.show()

'''
O código acima demonstra como criar histogramas para comparar a distribuição de pesos entre dois grupos diferentes: ginastas masculinos e remadores masculinos. Utilizando a biblioteca Matplotlib, o código lê os dados de arquivos CSV, plota histogramas sobrepostos para cada grupo e rotula os eixos para melhor compreensão. Isso permite uma análise visual eficaz das diferenças na distribuição de peso entre os dois esportes.
'''