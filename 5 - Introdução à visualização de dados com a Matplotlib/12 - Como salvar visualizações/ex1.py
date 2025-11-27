import matplotlib.pyplot as plt
import pandas as pd

medals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\medals_by_country_2016.csv', index_col=0)

fig, ax = plt.subplots()
ax.set_xticklabels(medals.index, rotation=90)

# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals['Gold'], label='Gold')

plt.show()

# Save as a PNG file
fig.savefig('my_figure.png')

# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png', dpi=300)

'''
O código acima demonstra como salvar uma visualização criada com Matplotlib em diferentes formatos e resoluções. Após criar um gráfico de barras que exibe o número de medalhas de ouro conquistadas por país nas Olimpíadas de 2016, o gráfico é salvo como um arquivo PNG padrão e também como um arquivo PNG com uma resolução mais alta de 300 dpi. Isso é útil para garantir que as visualizações mantenham sua qualidade ao serem compartilhadas ou publicadas.
'''