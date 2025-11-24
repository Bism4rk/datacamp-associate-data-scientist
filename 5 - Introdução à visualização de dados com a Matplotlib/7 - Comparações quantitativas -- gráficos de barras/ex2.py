import matplotlib.pyplot as plt
import pandas as pd

medals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\medals_by_country_2016.csv', index_col=0)

fig, ax = plt.subplots()
ax.set_xticklabels(medals.index, rotation=90)


# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals['Gold'], label='Gold')

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], label='Silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'], bottom=medals['Gold']+medals['Silver'], label='Bronze')

# Display the legend
ax.legend()

plt.show()

'''
O código acima demonstra como criar um gráfico de barras empilhadas para visualizar o número total de medalhas (ouro, prata e bronze) conquistadas por diferentes países nas Olimpíadas de 2016. Utilizando a biblioteca Matplotlib, o gráfico apresenta as medalhas empilhadas no eixo y e os países no eixo x, com uma legenda que identifica cada tipo de medalha. Essa visualização facilita a comparação quantitativa do desempenho olímpico entre os países, destacando tanto o total de medalhas quanto a distribuição entre os tipos.
'''