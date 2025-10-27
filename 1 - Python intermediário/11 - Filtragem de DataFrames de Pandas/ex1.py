# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

'''
O código acima demonstra como filtrar um DataFrame do Pandas com base em uma condição booleana. Primeiro, ele importa os dados de um arquivo CSV para um DataFrame chamado 'cars'. Em seguida, extrai a coluna 'drives_right' como uma Série chamada 'dr', que contém valores booleanos indicando se o carro dirige do lado direito. Em seguida, o código usa essa Série booleana para filtrar o DataFrame 'cars', selecionando apenas as linhas onde 'drives_right' é True. Finalmente, ele imprime o DataFrame filtrado 'sel', que contém apenas os carros que dirigem do lado direito.
'''