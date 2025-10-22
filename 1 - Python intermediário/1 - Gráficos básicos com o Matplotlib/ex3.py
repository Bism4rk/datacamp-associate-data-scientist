from things import life_exp, gdp_cap
import matplotlib.pyplot as plt

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

'''
O código acima demonstra como criar um gráfico de linha simples usando Matplotlib em Python. Ele importa duas listas, `gdp_cap` e `life_exp`, que representam o PIB per capita e a expectativa de vida, respectivamente. O código imprime os últimos valores dessas listas, cria um gráfico de linha com `gdp_cap` no eixo x e `life_exp` no eixo y, e finalmente exibe o gráfico. Nesse caso, vemos que o gráfico de linha pode não ser a melhor escolha para esses dados, pois eles não representam uma série temporal ou uma relação contínua, levando a uma apresentação confusa.
'''