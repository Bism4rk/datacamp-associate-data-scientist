import pandas as pd

dogs = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\dogs.csv')

# Fix the misspelled word
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs["sex"].replace(replace_map)

# Strip away leading whitespace
dogs["sex"] = dogs["sex"].str.strip()

# Make all responses lowercase
dogs["sex"] = dogs["sex"].str.lower()

# Convert to a categorical Series
dogs["sex"] = dogs['sex'].astype('category')

print(dogs["sex"].value_counts())

'''
O código acima demonstra como limpar dados categóricos em um DataFrame do pandas. Primeiro, ele corrige um erro de digitação na coluna sex, substituindo "Malez" por "male" usando um dicionário de mapeamento. Em seguida, remove espaços em branco no início e no final das strings na coluna sex. Depois, converte todas as entradas para letras minúsculas para garantir consistência. Finalmente, converte a coluna sex em uma variável categórica e imprime a tabela de frequência das categorias na coluna.
'''