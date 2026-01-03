import pandas as pd

# Assign the filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.to_numpy()

# Print the datatype of data_array to the shell
print(type(data_array))

'''
O código acima demonstra como importar um arquivo CSV contendo dados de dígitos usando a biblioteca Pandas em Python. Primeiro, o pandas é importado com o alias 'pd'. Em seguida, o caminho completo do arquivo CSV é atribuído à variável 'file'. O arquivo é lido e as primeiras 5 linhas são carregadas em um DataFrame chamado 'data' usando a função pd.read_csv() com os parâmetros nrows=5 e header=None para indicar que não há cabeçalho no arquivo. Depois, o DataFrame é convertido em um array numpy usando o método to_numpy() e armazenado na variável 'data_array'. Finalmente, o tipo de 'data_array' é impresso no console para confirmar que é um array numpy.
'''