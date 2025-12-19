import pandas as pd

dogs = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\dogs.csv')

# Create the my_changes dictionary
my_changes = {"Maybe?": "Maybe"}

dogs['likes_children'] = dogs['likes_children'].astype('category')

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs['likes_children'].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs['likes_children'].cat.categories)

'''
O código acima demonstra como renomear categorias em uma variável categórica usando o pandas. Primeiro, ele cria um dicionário chamado my_changes para mapear categorias antigas para novas. Em seguida, converte a coluna 'likes_children' em uma variável categórica. Depois, usa o método rename_categories para renomear as categorias com base no dicionário my_changes. Além disso, aplica uma função lambda para converter todas as categorias para letras maiúsculas. Finalmente, imprime a lista atualizada de categorias.
'''