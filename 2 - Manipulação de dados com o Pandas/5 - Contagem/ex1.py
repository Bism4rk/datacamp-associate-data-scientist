import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates['date'])

'''
O código acima demonstra como identificar e remover duplicatas em um DataFrame do Pandas com base em combinações específicas de colunas. Primeiro, ele remove duplicatas com base na combinação das colunas 'store' e 'type', exibindo as primeiras linhas do resultado. Em seguida, ele faz o mesmo para a combinação das colunas 'store' e 'department'. Finalmente, o código filtra as linhas onde a coluna 'is_holiday' é verdadeira, remove duplicatas com base na coluna 'date' e imprime as datas únicas correspondentes aos feriados.
'''