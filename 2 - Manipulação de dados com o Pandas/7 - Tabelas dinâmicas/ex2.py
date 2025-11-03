import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="type", columns="department", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))

'''
O código acima demonstra como criar tabelas dinâmicas (pivot tables) usando o Pandas para analisar dados de vendas semanais. Primeiro, ele lê um conjunto de dados de vendas e cria uma tabela dinâmica que calcula a média das vendas semanais, segmentada por tipo de loja e departamento, preenchendo quaisquer valores ausentes com 0, e imprime essa tabela. Em seguida, o código cria outra tabela dinâmica semelhante, mas desta vez inverte as dimensões (departamento como índice e tipo como colunas), também preenchendo valores ausentes com 0, e adiciona totais gerais para todas as linhas e colunas, imprimindo o resultado final.
'''