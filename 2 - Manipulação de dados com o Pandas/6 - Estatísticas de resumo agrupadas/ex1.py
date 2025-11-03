import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

'''
O código acima demonstra como calcular a proporção de vendas semanais totais para diferentes tipos de lojas em um DataFrame do Pandas. Primeiro, ele lê um conjunto de dados de vendas e calcula o total de vendas semanais. Em seguida, ele cria subconjuntos dos dados para cada tipo de loja (A, B e C) e calcula o total de vendas semanais para cada tipo. Finalmente, o código calcula a proporção das vendas semanais de cada tipo em relação ao total geral e imprime essas proporções.
'''
