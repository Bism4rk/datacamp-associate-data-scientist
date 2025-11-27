import matplotlib.pyplot as plt
import pandas as pd

medals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\medals_by_country_2016.csv', index_col=0)

fig, ax = plt.subplots()
ax.set_xticklabels(medals.index, rotation=90)

# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals['Gold'], label='Gold')

plt.show()

# Set figure dimensions and save as a PNG
fig.set_size_inches([3, 5]) # type: ignore
fig.savefig('figure_3_5.png')

# Set figure dimensions and save as a PNG
fig.set_size_inches([5, 3]) # type: ignore
fig.savefig('figure_5_3.png')

'''
O código acima demonstra como ajustar as dimensões de uma figura criada com Matplotlib antes de salvá-la. Após criar um gráfico de barras que exibe o número de medalhas de ouro conquistadas por país nas Olimpíadas de 2016, o gráfico é salvo em dois formatos diferentes: um com dimensões de 3 polegadas por 5 polegadas e outro com dimensões de 5 polegadas por 3 polegadas. Isso permite que o usuário escolha a melhor proporção para a visualização, dependendo do contexto em que será utilizada.
'''