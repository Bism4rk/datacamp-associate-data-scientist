# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

'''
O código acima demonstra como importar dados de uma planilha Excel em Python usando a biblioteca pandas. Primeiro, o arquivo da planilha é especificado. Em seguida, a planilha é carregada usando a função pd.ExcelFile(). Depois, duas abas (sheets) diferentes da planilha são carregadas em DataFrames: uma pelo nome da aba ('2004') e outra pelo índice (0). Finalmente, as primeiras linhas de ambos os DataFrames são impressas na tela.
'''