# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

'''
O código acima novamente cria dois arrays NumPy, dessa vez representando as áreas de diferentes cômodos em duas casas. Em seguida, ele utiliza operadores de comparação para gerar arrays booleanos que indicam se cada cômodo da "minha casa" tem uma área maior ou igual a 18 metros quadrados e se cada cômodo da "minha casa" tem uma área menor que a correspondente na "sua casa". Os resultados são impressos no console.
'''