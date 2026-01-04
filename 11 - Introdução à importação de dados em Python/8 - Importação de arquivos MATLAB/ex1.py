# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\ja_data2.mat')

# Print the datatype type of mat
print(type(mat))

'''
O código acima demonstra como importar arquivos MATLAB (.mat) em Python usando o pacote scipy.io. A função loadmat é utilizada para carregar o arquivo MATLAB especificado, e o tipo de dado resultante é impresso, que geralmente é um dicionário contendo as variáveis armazenadas no arquivo MATLAB.
'''
