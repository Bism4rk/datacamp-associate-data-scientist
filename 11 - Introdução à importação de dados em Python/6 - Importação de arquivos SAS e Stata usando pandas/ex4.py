# Import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

'''
O código acima demonstra como importar um arquivo Stata (.dta) usando a biblioteca pandas em Python. Primeiro, o arquivo é lido e convertido em um DataFrame do pandas. Em seguida, a função head() é usada para exibir as primeiras linhas do DataFrame, permitindo uma visualização rápida dos dados importados. Finalmente, um histograma da coluna 'disa10' do DataFrame é plotado usando matplotlib para analisar a distribuição dos valores nessa coluna.
'''