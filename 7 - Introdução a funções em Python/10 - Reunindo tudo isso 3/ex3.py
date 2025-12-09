# Import pandas
import pandas as pd

tweets_df = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\7 - Introdução a funções em Python\\3 - Reunindo tudo isso\\tweets.csv')

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

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

# # Print result1
# print(result1)

print(tweets_df[['lang', 'created_at']])

'''
O código acima define uma função `count_entries()` que conta as ocorrências de cada valor em uma coluna específica de um DataFrame do pandas. A função verifica se a coluna especificada existe no DataFrame e, se não existir, levanta um erro do tipo `ValueError` com uma mensagem apropriada. Se a coluna existir, a função itera sobre seus valores, atualizando um dicionário com as contagens correspondentes. Finalmente, a função é chamada com o DataFrame de tweets e o resultado é impresso.
'''