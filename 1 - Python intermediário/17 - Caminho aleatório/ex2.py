import numpy as np
np.random.seed(123)

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

'''
O código acima melhora a simulação de uma caminhada aleatória de 100 passos, garantindo que a posição nunca seja negativa. Isso é feito usando a função max() para assegurar que, ao tentar mover um passo para trás, a posição mínima seja 0. O restante da lógica permanece a mesma, onde o próximo passo é determinado pelo resultado de um lançamento de dado. O resultado final é uma lista que representa a posição ao longo do tempo dessa caminhada aleatória, sem jamais cair abaixo de zero.
'''