# Import numpy as np
import numpy as np

np_height = np.array([74, 76, 72, 73, 75])
np_baseball = np.array([[180, 78.4],
                        [215, 102.7],
                        [210, 98.5],
                        [188, 75.2],
                        [176, 70.0]])

# For loop over np_height
for h in np_height:
    print(str(h) + " inches")

# For loop over np_baseball
for b in np.nditer(np_baseball):
    print(b)

'''
O código acima demonstra como usar loops for para iterar sobre arrays NumPy. No primeiro loop, ele percorre um array unidimensional de alturas e imprime cada altura em polegadas. No segundo loop, ele utiliza np.nditer() para iterar sobre um array bidimensional que representa dados de beisebol, imprimindo cada elemento individualmente.
'''