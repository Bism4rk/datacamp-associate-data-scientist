# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

'''
O código acima demonstra como importar um arquivo CSV contendo dados do Titanic usando a biblioteca Pandas em Python. Primeiro, o pandas é importado com o alias 'pd'. Em seguida, o caminho completo do arquivo CSV é atribuído à variável 'file'. O arquivo é lido e carregado em um DataFrame chamado 'df' usando a função pd.read_csv(). Finalmente, as primeiras linhas do DataFrame são exibidas no console com o método head().
'''