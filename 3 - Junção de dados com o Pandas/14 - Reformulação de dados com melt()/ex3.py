import pandas as pd
import matplotlib.pyplot as plt

ten_yr = pd.read_csv('placeholder/ten_yr_bond.csv')
dji = pd.read_csv('placeholder/dow_jones.csv')

# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', how='inner', suffixes=('_dow', '_bond'))

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()

'''
O código acima demonstra como transformar e combinar conjuntos de dados financeiros usando o Pandas. Primeiro, os dados de títulos de 10 anos são carregados e reformulados usando a função melt() para "desempilhar" as colunas, mantendo a métrica como identificador. Em seguida, é aplicada uma consulta para selecionar apenas as linhas onde a métrica é "close". Depois disso, os dados do Dow Jones são mesclados com os dados dos títulos reformulados com base na coluna de data, utilizando uma junção interna ordenada. Finalmente, um gráfico é gerado para visualizar os preços de fechamento do Dow Jones e dos títulos ao longo do tempo.
'''