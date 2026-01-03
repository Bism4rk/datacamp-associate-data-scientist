# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

'''
O código acima demonstra como importar dados de uma planilha Excel em Python usando a biblioteca pandas. Primeiro, o arquivo da planilha é especificado. Em seguida, a planilha é carregada usando a função pd.ExcelFile(). Finalmente, os nomes das abas (sheets) da planilha são impressos na tela.
'''