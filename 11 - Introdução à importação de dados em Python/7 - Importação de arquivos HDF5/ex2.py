# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\L-L1_LOSC_4_V1-1126259446-32.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

'''
O código acima demonstra como importar e explorar arquivos HDF5 em Python usando a biblioteca h5py. Primeiro, o arquivo HDF5 é carregado e seu tipo de dado é impresso, confirmando que é um objeto h5py.File. Em seguida, as chaves principais do arquivo são listadas, permitindo ao usuário entender a estrutura dos dados armazenados no arquivo.
'''