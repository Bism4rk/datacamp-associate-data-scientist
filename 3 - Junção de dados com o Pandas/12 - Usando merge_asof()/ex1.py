import pandas as pd
import matplotlib.pyplot as plt

# not actual datasets, just here to illustrate the code structure and stop errors
jpm = pd.read_csv('data/jpm.csv', parse_dates=['date_time'])
wells = pd.read_csv('data/wells.csv', parse_dates=['date_time'])
bac = pd.read_csv('data/bac.csv', parse_dates=['date_time'])

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', suffixes=('_jpm', '_bac'), direction='nearest')

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()

'''
O código acima demonstra como usar a função merge_asof() do Pandas para combinar três conjuntos de dados financeiros (JPM, Wells Fargo e Bank of America) com base em timestamps próximos. Após a fusão dos dados, calcula-se a diferença de preços entre os registros consecutivos e plota-se essa diferença para as ações de cada banco. Isso é útil para analisar variações de preços ao longo do tempo em relação a eventos específicos ou tendências de mercado. O merge_asof() é particularmente eficaz para séries temporais, onde os dados podem não estar perfeitamente alinhados em termos de tempo.
'''