from matplotlib import pyplot as plt
from things import life_exp

# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()

'''
O código acima demonstra como criar e exibir histogramas com diferentes números de bins (intervalos) usando a biblioteca Matplotlib em Python. Ele importa uma lista de expectativas de vida (life_exp) do módulo things.py, cria um histograma dessa lista com 5 bins e o exibe. Em seguida, ele limpa o gráfico e cria outro histograma com 20 bins, exibindo-o novamente. A variação no número de bins permite observar como a granularidade da distribuição dos dados muda, oferecendo diferentes perspectivas sobre a mesma informação.
'''