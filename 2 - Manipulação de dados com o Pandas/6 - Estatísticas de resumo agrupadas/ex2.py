import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

'''
O código acima demonstra como calcular a proporção de vendas semanais totais para diferentes tipos de lojas em um DataFrame do Pandas, bem como como agrupar os dados por múltiplas colunas. Primeiro, ele lê um conjunto de dados de vendas e agrupa os dados pela coluna 'type', calculando o total de vendas semanais para cada tipo de loja. Em seguida, calcula a proporção das vendas semanais de cada tipo em relação ao total geral e imprime essas proporções. Depois, o código agrupa os dados por ambas as colunas 'type' e 'is_holiday', calculando o total de vendas semanais para cada combinação dessas categorias, e imprime os resultados.
'''