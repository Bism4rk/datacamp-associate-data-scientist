from matplotlib import pyplot as plt
from things import gdp_cap, life_exp

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

'''
O código acima demonstra como customizar um gráfico de dispersão usando Matplotlib em Python. Ele inclui:
1. Importação das bibliotecas necessárias.
2. Criação de um gráfico de dispersão dos dados de PIB per capita e expectativa de vida.
3. Configuração da escala logarítmica para o eixo x.
4. Definição de rótulos para os eixos x e y.
5. Adição de um título ao gráfico.
6. Exibição do gráfico finalizado.

Com isso, o gráfico se torna mais informativo e visualmente atraente.
'''