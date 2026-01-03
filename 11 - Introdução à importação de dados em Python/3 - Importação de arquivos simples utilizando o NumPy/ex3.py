import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\seaslugs.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import file as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype='float', skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

'''
O código acima demonstra como importar dados de um arquivo de texto simples usando a biblioteca NumPy em Python. Primeiro, o arquivo 'seaslugs.txt' é carregado como uma matriz de strings, e o primeiro elemento é impresso. Em seguida, o mesmo arquivo é importado novamente, mas desta vez como uma matriz de floats, ignorando a primeira linha (cabeçalho). O décimo elemento dessa matriz é impresso. Finalmente, um gráfico de dispersão é criado para visualizar a relação entre o tempo (em minutos) e a porcentagem de larvas, utilizando a biblioteca Matplotlib.
'''