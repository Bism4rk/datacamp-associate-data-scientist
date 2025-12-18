import pandas as pd

adult = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\adult.csv')

# Explore the Above/Below 50k variable
print(adult["Above/Below 50k"].describe())

# Print a frequency table of "Above/Below 50k"
print(adult["Above/Below 50k"].value_counts())

# Print relative frequency values
print(adult["Above/Below 50k"].value_counts(normalize=True))

'''
O código acima demonstra como carregar um conjunto de dados em um DataFrame do pandas e explorar uma variável categórica específica chamada "Above/Below 50k". Ele começa importando a biblioteca pandas e lendo um arquivo CSV contendo os dados. Em seguida, ele imprime uma descrição estatística da variável categórica, seguida por uma tabela de frequência que mostra a contagem de cada categoria dentro da variável. Finalmente, o código calcula e imprime as frequências relativas das categorias, fornecendo uma visão percentual da distribuição dos dados nessa variável.
'''