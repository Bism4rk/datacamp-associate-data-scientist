import pandas as pd

sales_1_1 = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv').head(10)

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

'''
O código acima demonstra como calcular somas e máximos cumulativos em um DataFrame do Pandas. Primeiro, ele lê um subconjunto de dados de vendas e ordena os dados pela coluna 'date'. Em seguida, calcula a soma cumulativa da coluna 'weekly_sales' e a armazena em uma nova coluna chamada 'cum_weekly_sales'. Além disso, calcula o valor máximo cumulativo da mesma coluna e o armazena em outra nova coluna chamada 'cum_max_sales'. Finalmente, o código imprime as colunas relevantes para mostrar os resultados dos cálculos.
'''