# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file: # não é um arquivo real, apenas um exemplo
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

'''
O código acima demonstra como importar dados de um arquivo pickle em Python. Primeiro, o pacote pickle é importado. Em seguida, o arquivo 'data.pkl' é aberto em modo de leitura binária ('rb') e os dados são carregados usando a função pickle.load(). Finalmente, os dados carregados e seu tipo de dado são impressos na tela.
'''