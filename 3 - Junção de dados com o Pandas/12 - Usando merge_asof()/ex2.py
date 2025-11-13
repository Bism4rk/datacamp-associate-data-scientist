import pandas as pd
import matplotlib.pyplot as plt

# not actual datasets, just here to illustrate the code structure and stop errors
gdp = pd.read_csv('data/gdp.csv', parse_dates=['date'])
recession = pd.read_csv('data/recession.csv', parse_dates=['date'])

# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on='date')

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
plt.show()

'''
O código acima demonstra como usar a função merge_asof() do Pandas para combinar dois conjuntos de dados econômicos: o PIB (Produto Interno Bruto) e os períodos de recessão. A fusão é feita com base na coluna de datas, permitindo alinhar os dados do PIB com o status econômico correspondente (recessão ou crescimento). Em seguida, um gráfico de barras é criado para visualizar o PIB ao longo do tempo, com as barras coloridas de acordo com o status econômico (vermelho para recessão e verde para crescimento). Isso facilita a análise visual das variações do PIB em relação aos períodos econômicos.
'''