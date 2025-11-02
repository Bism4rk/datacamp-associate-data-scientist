import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)

print(dept_props_sorted)

'''
O código acima demonstra como contar valores únicos em um DataFrame do Pandas usando o método `value_counts()`. Primeiro, ele remove duplicatas com base nas combinações das colunas 'store' e 'type', e depois conta o número de lojas de cada tipo, exibindo os resultados. Em seguida, ele calcula a proporção de lojas de cada tipo. O mesmo processo é repetido para as combinações das colunas 'store' e 'department', contando o número de lojas em cada departamento e calculando suas proporções, ambos os resultados sendo ordenados.
'''