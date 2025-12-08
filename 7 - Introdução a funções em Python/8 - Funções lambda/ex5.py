# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)

'''
O código acima demonstra como usar a função `reduce()` em conjunto com uma função lambda para concatenar todos os elementos de uma lista de strings. A lista `stark` contém nomes de personagens, e a função lambda combina dois elementos de cada vez, resultando em uma única string que contém todos os nomes concatenados. A string resultante é então impressa.
'''