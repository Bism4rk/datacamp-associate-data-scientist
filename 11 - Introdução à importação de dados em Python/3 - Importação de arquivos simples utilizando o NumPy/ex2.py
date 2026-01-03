# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt' # não é o arquivo real, apenas um exemplo

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# Print data
print(data)

'''
O código acima demonstrates como importar dados de um arquivo de texto simples usando a biblioteca NumPy em Python. Ele carrega apenas as colunas 0 e 2 do arquivo, ignorando a primeira linha (cabeçalho) e utilizando o caractere de tabulação como delimitador.
'''