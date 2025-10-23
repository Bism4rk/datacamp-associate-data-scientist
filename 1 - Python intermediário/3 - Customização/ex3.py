import matplotlib.pyplot as plt
from things import gdp_cap, life_exp, pop

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

'''
O código acima demonstra como ajustar o tamanho dos pontos em um gráfico de dispersão usando Matplotlib em Python. Ele constrói sobre as customizações anteriores, incluindo:
1. Importação das bibliotecas necessárias, incluindo NumPy.
2. Conversão da lista de população em um array NumPy.
3. Duplicação dos valores de população para aumentar o tamanho dos pontos.
4. Criação de um gráfico de dispersão dos dados de PIB per capita e expectativa de vida, com o tamanho dos pontos definido pela população.
5. Manutenção das customizações anteriores, como escala logarítmica, rótulos dos eixos, título e ticks personalizados.
6. Exibição do gráfico finalizado.

Com isso, o gráfico se torna mais informativo e visualmente atraente, refletindo a população através do tamanho dos pontos.
'''