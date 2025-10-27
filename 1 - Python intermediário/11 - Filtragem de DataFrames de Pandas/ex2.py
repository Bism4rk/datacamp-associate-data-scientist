# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right'] == True]

# Print sel
print(sel)

'''
O código acima melhora a legibilidade e concisão ao converter o processo de filtragem do DataFrame 'cars' em uma única linha. Em vez de criar uma variável intermediária para armazenar a Série booleana, ele diretamente utiliza a condição booleana dentro dos colchetes para filtrar o DataFrame. Isso resulta em um código mais compacto que realiza a mesma tarefa: selecionar apenas as linhas onde a coluna 'drives_right' é True, e então imprime o DataFrame filtrado 'sel'.
'''