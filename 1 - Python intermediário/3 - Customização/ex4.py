from matplotlib import pyplot as plt
from things import gdp_cap, life_exp, pop, col
import numpy as np

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha=0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

'''
O código acima demonstra como personalizar ainda mais um gráfico de dispersão usando Matplotlib em Python. Ele inclui:
1. Importação das bibliotecas necessárias.
2. Criação de um gráfico de dispersão dos dados de PIB per capita e expectativa de vida, com o tamanho dos pontos definido pela população, a cor definida por uma lista de cores e a transparência ajustada com o parâmetro alpha.
3. Manutenção das customizações anteriores, como escala logarítmica, rótulos dos eixos, título e ticks personalizados.
4. Exibição do gráfico finalizado.

Com isso, o gráfico se torna mais informativo e visualmente atraente, refletindo a população através do tamanho dos pontos, diferenciando categorias com cores e melhorando a estética com transparência.
'''