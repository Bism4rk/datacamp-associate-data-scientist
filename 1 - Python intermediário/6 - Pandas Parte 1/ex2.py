import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
# print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels # type: ignore

# Print cars again
print(cars)

'''
O código acima demonstra como definir rótulos personalizados para as linhas de um DataFrame do pandas. Primeiro, um DataFrame chamado `cars` é criado a partir de um dicionário contendo informações sobre países, se dirigem do lado direito e o número de carros por 1000 habitantes. Em seguida, uma lista chamada `row_labels` é definida, contendo os rótulos desejados para cada linha do DataFrame. Esses rótulos são então atribuídos ao índice do DataFrame `cars` usando `cars.index = row_labels`. Finalmente, o DataFrame atualizado é impresso na tela, agora exibindo os rótulos personalizados para cada linha.
'''