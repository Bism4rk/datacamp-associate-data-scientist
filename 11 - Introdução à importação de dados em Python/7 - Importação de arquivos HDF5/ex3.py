# Import packages
import numpy as np
import matplotlib.pyplot as plt
import h5py

# Assign filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\L-L1_LOSC_4_V1-1126259446-32.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys(): # type: ignore
    print(key)

# Set variable equal to time series data: strain
strain = np.array(data['strain']['Strain']) # type: ignore

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

'''
O código acima demonstra como importar e visualizar dados de um arquivo HDF5 usando a biblioteca h5py em Python. Primeiro, o arquivo HDF5 é carregado e o grupo 'strain' é acessado para explorar suas chaves. Em seguida, os dados de deformação são extraídos e convertidos em um array NumPy. Um vetor de tempo é criado para corresponder aos primeiros 10.000 pontos de dados, que são então plotados usando Matplotlib para visualizar a deformação ao longo do tempo.
'''