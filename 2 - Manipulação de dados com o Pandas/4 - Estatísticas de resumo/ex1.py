import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())

'''
O código acima demonstra como carregar um conjunto de dados de vendas a partir de um arquivo CSV usando a biblioteca Pandas em Python. Ele exibe as primeiras linhas do DataFrame para fornecer uma visão geral dos dados, além de informações sobre o DataFrame, como o número de entradas e tipos de dados. Finalmente, o código calcula e imprime a média e a mediana das vendas semanais, oferecendo insights estatísticos básicos sobre o desempenho das vendas.
'''
