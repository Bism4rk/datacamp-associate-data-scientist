# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Parse the first sheet and rename the columns: df1
df1 = xls.parse('2002', skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

'''
O código acima demonstra como importar dados de uma planilha Excel em Python usando a biblioteca pandas. Primeiro, o arquivo da planilha é especificado. Em seguida, a planilha é carregada usando a função pd.ExcelFile(). Depois, a primeira aba (sheet) da planilha é analisada (parse) para criar um DataFrame, pulando a primeira linha e renomeando as colunas. O mesmo processo é repetido para a segunda aba, mas apenas a primeira coluna é selecionada. Finalmente, as primeiras linhas de ambos os DataFrames são impressas na tela.
'''