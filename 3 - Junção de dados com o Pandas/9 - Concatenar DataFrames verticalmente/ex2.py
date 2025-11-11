import pandas as pd
import matplotlib.pyplot as plt

inv_jul = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\9 - Concatenar DataFrames verticalmente\\inv_jul.csv')
inv_aug = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\9 - Concatenar DataFrames verticalmente\\inv_aug.csv')
inv_sep = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\9 - Concatenar DataFrames verticalmente\\inv_sep.csv')

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()

'''
O código acima demonstra como concatenar três DataFrames de faturas mensais (julho, agosto e setembro) usando o Pandas, adicionando chaves para identificar cada mês. Em seguida, ele agrupa os dados concatenados pelo nível das chaves e calcula a média da coluna 'total' para cada mês. Finalmente, o código cria um gráfico de barras para visualizar a média das faturas por mês.
'''