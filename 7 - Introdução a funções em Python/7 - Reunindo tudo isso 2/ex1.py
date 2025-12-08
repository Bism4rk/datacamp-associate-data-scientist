# Import pandas
import pandas as pd

tweets_df = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\7 - Introdução a funções em Python\\3 - Reunindo tudo isso\\tweets.csv')

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)

'''
O código acima demonstra como definir uma função em Python para contar a frequência de diferentes valores em uma coluna específica de um DataFrame do pandas. A função `count_entries` recebe um DataFrame e o nome da coluna como argumentos, com um valor padrão definido para o nome da coluna. Dentro da função, um dicionário vazio é inicializado para armazenar as contagens. A coluna especificada é extraída do DataFrame e iterada. Para cada entrada, se o valor já estiver presente no dicionário, sua contagem é incrementada; caso contrário, o valor é adicionado ao dicionário com uma contagem inicial de 1. Finalmente, a função retorna o dicionário populado com as contagens. A função é então chamada duas vezes: uma vez usando o valor padrão para a coluna e outra vez especificando uma coluna diferente, e os resultados são impressos.
'''