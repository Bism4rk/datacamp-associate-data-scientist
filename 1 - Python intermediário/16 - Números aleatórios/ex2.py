# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))


'''
O código acima demonstra como usar a função randint() da biblioteca numpy para simular o lançamento de um dado. A função randint(a, b) gera um número inteiro aleatório no intervalo [a, b), ou seja, inclui o valor a, mas exclui o valor b. No exemplo, estamos simulando o lançamento de um dado de seis faces, portanto usamos randint(1, 7) para obter números entre 1 e 6.  
'''