from matplotlib import pyplot as plt
from things import gdp_cap, life_exp

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()

'''
O código acima demonstra como adicionar ticks personalizados ao eixo x de um gráfico de dispersão usando Matplotlib em Python. Ele inclui:
1. Importação das bibliotecas necessárias.
2. Criação de um gráfico de dispersão dos dados de PIB per capita e expectativa de vida.
3. Configuração da escala logarítmica para o eixo x.
4. Definição de rótulos para os eixos x e y.
5. Adição de um título ao gráfico.
6. Definição de valores e rótulos personalizados para os ticks do eixo x.
7. Exibição do gráfico finalizado.

Com isso, o gráfico se torna mais informativo e visualmente atraente.
'''