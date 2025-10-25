# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': names,
    'drives_right': dr,
    'cars_per_cap': cpc
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

'''
O código acima demonstra como criar um DataFrame do pandas a partir de um dicionário em Python. Primeiro, listas pré-definidas contendo nomes de países, uma coluna booleana indicando se o país dirige do lado direito e o número de carros por 1000 habitantes são criadas. Em seguida, essas listas são combinadas em um dicionário chamado `my_dict`, onde cada chave representa o nome da coluna e o valor é a lista correspondente. Finalmente, o DataFrame `cars` é construído a partir do dicionário usando `pd.DataFrame(my_dict)` e impresso na tela.
'''