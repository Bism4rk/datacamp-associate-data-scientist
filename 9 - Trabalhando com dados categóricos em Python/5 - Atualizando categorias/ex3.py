import pandas as pd

dogs = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\dogs.csv')

dogs['coat'] = dogs['coat'].astype('category')

# Create the update_coats dictionary
update_coats = {"wirehaired": "medium", "medium-long": "medium"}

# Create a new column, coat_collapsed
dogs["coat_collapsed"] = dogs['coat'].replace(update_coats)

# Convert the column to categorical
dogs['coat_collapsed'] = dogs['coat_collapsed'].astype('category')

# Print the frequency table
print(dogs['coat_collapsed'].value_counts())

'''
O código acima demonstra como agrupar categorias em uma variável categórica usando o pandas. Primeiro, ele cria um dicionário chamado update_coats para mapear categorias específicas para uma categoria mais geral. Em seguida, cria uma nova coluna chamada coat_collapsed, onde as categorias da coluna coat são substituídas de acordo com o dicionário update_coats. Depois, converte a nova coluna em uma variável categórica. Finalmente, imprime a tabela de frequência das categorias na coluna coat_collapsed.
'''