# Import package
import matplotlib.pyplot as plt
from things import life_exp2, pop2

# Build Scatter plot
plt.scatter(pop2, life_exp2)

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de dispersão (scatter plot) usando Matplotlib em Python. Ele importa duas listas, `pop2` e `life_exp2`, que representam a população e a expectativa de vida, respectivamente. O código cria um gráfico de dispersão com `pop2` no eixo x e `life_exp2` no eixo y, e finalmente exibe o gráfico. Esse tipo de gráfico é útil para visualizar a relação entre duas variáveis quantitativas, permitindo identificar padrões ou correlações entre elas.
'''