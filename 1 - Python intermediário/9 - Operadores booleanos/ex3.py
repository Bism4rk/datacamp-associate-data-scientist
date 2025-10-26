# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

'''
O código acima demonstra o uso de operadores booleanos com arrays em Python utilizando a biblioteca NumPy. Ele cria dois arrays, my_house e your_house, que representam os tamanhos de diferentes casas em metros quadrados. Em seguida, realiza duas comparações usando os operadores lógicos 'logical_or' e 'logical_and', e imprime os resultados dessas comparações.
'''