import numpy as np
np.random.seed(123)

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

'''
O código acima simula uma caminhada aleatória de 100 passos, onde cada passo é determinado pelo resultado de um lançamento de dado. Dependendo do valor do dado, o próximo passo pode ser um movimento para trás, um movimento para frente ou um salto maior para frente. O resultado final é uma lista que representa a posição ao longo do tempo dessa caminhada aleatória.
'''