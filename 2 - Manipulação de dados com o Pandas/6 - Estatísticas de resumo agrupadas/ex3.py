import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby(["type"])["weekly_sales"].agg([min, max, 'mean', 'median'])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby(["type"])[["unemployment", "fuel_price_usd_per_l"]].agg([min, max, 'mean', 'median'])

# Print unemp_fuel_stats
print(unemp_fuel_stats)

'''
O código acima demonstra como calcular estatísticas de resumo agrupadas em um DataFrame do Pandas. Primeiro, ele lê um conjunto de dados de vendas e agrupa os dados pela coluna 'type', calculando várias estatísticas (mínimo, máximo, média e mediana) para a coluna 'weekly_sales' e imprime os resultados. Em seguida, o código realiza uma agregação semelhante para as colunas 'unemployment' e 'fuel_price_usd_per_l', calculando as mesmas estatísticas para cada tipo de loja e imprimindo os resultados.
'''