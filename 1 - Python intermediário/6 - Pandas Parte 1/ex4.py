# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)

# Print out cars
print(cars)

'''
O código acima demonstra como importar um arquivo CSV para um DataFrame do pandas, especificando uma coluna para ser usada como índice. Primeiro, a biblioteca pandas é importada com o alias 'pd'. Em seguida, o arquivo 'cars.csv' é lido usando a função `pd.read_csv()`, com o parâmetro `index_col=0` para indicar que a primeira coluna do arquivo deve ser usada como índice do DataFrame. O DataFrame resultante é armazenado na variável `cars`. Finalmente, o conteúdo do DataFrame `cars` é impresso na tela, exibindo os dados contidos no arquivo CSV com a primeira coluna como índice.
'''