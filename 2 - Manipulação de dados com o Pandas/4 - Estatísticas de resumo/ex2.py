import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())

'''
O código acima carrega um conjunto de dados de vendas a partir de um arquivo CSV usando a biblioteca Pandas em Python. Ele calcula e imprime as datas máxima e mínima presentes na coluna 'date' do DataFrame, fornecendo informações sobre o intervalo temporal dos dados de vendas.
'''