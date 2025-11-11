import pandas as pd

employees = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\8 - Joins de filtragem\\employees.csv')
top_cust = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\8 - Joins de filtragem\\top_cust.csv')

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

'''
O código acima demonstra como fazer um anti-join usando o Pandas para identificar funcionários que não estão trabalhando com os principais clientes. Primeiro, os DataFrames 'employees' e 'top_cust' são mesclados usando um left join com o parâmetro 'indicator=True', que adiciona uma coluna '_merge' para indicar a origem de cada linha. Em seguida, selecionamos os 'srid' onde '_merge' é 'left_only', indicando que esses funcionários não têm correspondência em 'top_cust'. Finalmente, filtramos o DataFrame 'employees' para exibir apenas esses funcionários.
'''