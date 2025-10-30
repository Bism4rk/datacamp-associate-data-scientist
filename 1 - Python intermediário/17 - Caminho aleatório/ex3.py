import numpy as np
np.random.seed(123)

# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

'''
O código acima melhora o exercício anterior ao adicionar uma visualização do caminho aleatório usando a biblioteca Matplotlib. A biblioteca Matplotlib é importada como plt, e a função plt.plot() é usada para criar o gráfico do caminho aleatório armazenado na lista random_walk. Finalmente, plt.show() é chamado para exibir o gráfico.
'''