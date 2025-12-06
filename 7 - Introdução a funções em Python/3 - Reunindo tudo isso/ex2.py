# Import pandas
import pandas as pd

tweets_df = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\7 - Introdução a funções em Python\\3 - Reunindo tudo isso\\tweets.csv')

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)

'''
O código acima demonstra como definir uma função em Python para contar a frequência de diferentes valores em uma coluna específica de um DataFrame do pandas. A função `count_entries` recebe um DataFrame e o nome da coluna como argumentos. Dentro da função, um dicionário vazio é inicializado para armazenar as contagens. A coluna especificada é extraída do DataFrame e iterada. Para cada entrada, se o valor já estiver presente no dicionário, sua contagem é incrementada; caso contrário, o valor é adicionado ao dicionário com uma contagem inicial de 1. Finalmente, a função retorna o dicionário populado com as contagens, que é então impresso após a chamada da função.
'''