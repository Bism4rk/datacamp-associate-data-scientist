# Import package
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load MATLAB file: mat
mat = scipy.io.loadmat('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\ja_data2.mat')

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()


'''
O código acima demonstra como importar arquivos MATLAB (.mat) em Python usando o pacote scipy.io. Após carregar o arquivo, ele imprime as chaves do dicionário resultante, o tipo e a forma dos dados associados a uma chave específica ('CYratioCyt'). Em seguida, ele extrai uma parte dos dados e cria um gráfico de linha para visualizar a expressão normalizada ao longo do tempo.
'''