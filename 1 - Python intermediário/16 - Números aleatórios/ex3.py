import numpy as np
np.random.seed(123)

# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice < 6 :
    step += 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

'''
O código acima simula o movimento de um jogador em um jogo de tabuleiro baseado no lançamento de um dado. Dependendo do valor obtido no dado, o jogador pode mover-se para trás, para frente ou avançar um número adicional de casas. A estrutura condicional if-elif-else é usada para determinar o movimento do jogador com base no resultado do dado. 
'''