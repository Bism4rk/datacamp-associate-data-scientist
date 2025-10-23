from matplotlib import pyplot as plt
from things import gdp_cap, life_exp, pop, col
import numpy as np

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()

'''
O código acima demonstra como adicionar anotações e uma grade a um gráfico de dispersão usando Matplotlib em Python. Ele inclui:
1. Importação das bibliotecas necessárias.
2. Criação de um gráfico de dispersão dos dados de PIB per capita e expectativa de vida, com o tamanho dos pontos definido pela população, a cor definida por uma lista de cores e a transparência ajustada com o parâmetro alpha.
3. Manutenção das customizações anteriores, como escala logarítmica, rótulos dos eixos, título e ticks personalizados.
4. Adição de anotações para destacar os países Índia e China em posições específicas do gráfico.
5. Inclusão de uma grade no gráfico para melhorar a legibilidade dos dados.
6. Exibição do gráfico finalizado.

Com isso, o gráfico se torna mais informativo e visualmente atraente, refletindo a população através do tamanho dos pontos, diferenciando categorias com cores, melhorando a estética com transparência, destacando países específicos e facilitando a leitura dos dados com a grade.
'''