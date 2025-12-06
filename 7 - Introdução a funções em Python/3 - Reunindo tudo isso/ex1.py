# Import pandas
import pandas as pd

tweets = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\7 - Introdução a funções em Python\\3 - Reunindo tudo isso\\tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = tweets['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)

'''
O código acima demonstra como contar a frequência de diferentes idiomas em uma coluna de um DataFrame do pandas. Primeiro, ele importa a biblioteca pandas e lê um arquivo CSV contendo dados de tweets. Em seguida, inicializa um dicionário vazio para armazenar a contagem de idiomas. Depois, extrai a coluna 'lang' do DataFrame e itera sobre cada entrada nessa coluna. Se o idioma já estiver presente no dicionário, incrementa sua contagem em 1; caso contrário, adiciona o idioma ao dicionário com uma contagem inicial de 1. Finalmente, imprime o dicionário populado com as contagens de idiomas.
'''