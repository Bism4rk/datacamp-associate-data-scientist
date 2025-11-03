import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=['mean', 'median']) # type: ignore

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

'''
O código acima demonstra como criar tabelas dinâmicas (pivot tables) usando o Pandas para analisar dados de vendas semanais. Primeiro, ele lê um conjunto de dados de vendas e cria uma tabela dinâmica que calcula a média das vendas semanais para cada tipo de loja, imprimindo os resultados. Em seguida, ele cria outra tabela dinâmica que calcula tanto a média quanto a mediana das vendas semanais para cada tipo de loja, novamente imprimindo os resultados. Finalmente, o código cria uma tabela dinâmica que calcula a média das vendas semanais, segmentada por tipo de loja e se a semana é um feriado ou não, e imprime essa tabela. 
'''