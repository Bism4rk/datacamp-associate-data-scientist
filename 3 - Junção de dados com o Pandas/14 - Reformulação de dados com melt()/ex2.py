import pandas as pd
import matplotlib.pyplot as plt

ur_wide = pd.read_csv('placeholder/unempl_rate.csv')

# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars='year', var_name='month', value_name='unempl_rate')

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()

'''
O código acima demonstra como transformar um DataFrame de formato largo para formato longo usando a função melt() do Pandas. Primeiro, os dados são carregados de um arquivo CSV. Em seguida, a função melt() é utilizada para "desempilhar" as colunas de meses, mantendo o ano como identificador. Uma nova coluna de data é criada combinando o mês e o ano, que é então convertida para o formato datetime. Finalmente, os dados são ordenados por data e um gráfico é gerado para visualizar a taxa de desemprego ao longo do tempo.
'''