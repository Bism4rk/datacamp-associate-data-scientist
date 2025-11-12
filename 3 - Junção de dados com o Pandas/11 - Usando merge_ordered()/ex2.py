import pandas as pd
import matplotlib.pyplot as plt

inflation = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\inflation.csv')
unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\11 - Usando merge_ordered()\\unemployment.csv')

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, how='inner')

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
plt.show()

'''
O código acima demonstra como usar a função merge_ordered() do Pandas para combinar dois DataFrames, inflation e unemployment, com uma junção interna (inner join) baseada na coluna 'date'. Após a fusão, o DataFrame resultante, inflation_unemploy, é impresso e um gráfico de dispersão (scatter plot) é criado para visualizar a relação entre a taxa de desemprego (unemployment_rate) e o índice de preços ao consumidor (cpi).
'''