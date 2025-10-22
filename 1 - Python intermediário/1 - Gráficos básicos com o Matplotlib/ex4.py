from things import life_exp, gdp_cap
import matplotlib.pyplot as plt

# Change the line plot below to a scatter plot
plt.plot(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Show plot
plt.show()

'''
O código acima cria um gráfico de dispersão (scatter plot) usando Matplotlib em Python, representando a relação entre o PIB per capita (`gdp_cap`) e a expectativa de vida (`life_exp`). A escala do eixo x é alterada para uma escala logarítmica, o que é útil para visualizar dados que abrangem várias ordens de magnitude. O gráfico de dispersão é mais apropriado para esses dados do que um gráfico de linha, pois permite observar a distribuição e a correlação entre as duas variáveis de forma mais clara.
'''