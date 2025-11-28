# Import pandas
import pandas as pd

csv_filepath = 'https://assets.datacamp.com/production/repositories/3996/datasets/7ac19e11cf7ed61205ffe8da5208794b8e2a5086/1.2.1_example_csv.csv'

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())

'''
O código acima demonstra como importar a biblioteca pandas em Python, ler um arquivo CSV a partir de uma URL e criar um DataFrame com os dados contidos nesse arquivo. Em seguida, ele imprime as primeiras linhas do DataFrame usando o método head(), permitindo visualizar uma amostra dos dados carregados.
'''