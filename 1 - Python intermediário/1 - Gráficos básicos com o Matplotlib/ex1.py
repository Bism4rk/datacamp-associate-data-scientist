from things import year, pop

# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

'''
O código acima demonstra como criar um gráfico de linha simples usando a biblioteca Matplotlib em Python. Ele importa os dados de anos e populações de um módulo chamado "things", plota esses dados em um gráfico de linha e exibe o gráfico. Ele também imprime o último valor de cada lista para verificação. Plots são uma ferramenta poderosa para visualizar dados e identificar tendências ao longo do tempo.
'''
