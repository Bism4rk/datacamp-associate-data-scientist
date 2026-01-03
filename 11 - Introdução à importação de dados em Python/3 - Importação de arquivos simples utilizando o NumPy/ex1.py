# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\digits.txt'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

'''
O código acima demonstra como importar um arquivo de texto contendo dados numéricos usando o NumPy, selecionar uma linha específica, remodelá-la em uma matriz 2D e visualizá-la como uma imagem usando Matplotlib. Ele também imprime o tipo de dados do array carregado para confirmar que os dados foram importados corretamente.
''' 
