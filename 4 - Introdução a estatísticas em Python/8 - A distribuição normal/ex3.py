import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

amir_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\amir_deals.csv', index_col=0)

# Calculate new average amount
new_mean = 5000 * 1.2

# Calculate new standard deviation
new_sd = 2000 * 1.3

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()

'''
O código acima demonstra como ajustar a média e o desvio padrão de uma distribuição normal para simular novos dados. Primeiro, a média original de 5000 é aumentada em 20%, resultando em uma nova média de 6000. Em seguida, o desvio padrão original de 2000 é aumentado em 30%, resultando em um novo desvio padrão de 2600. Em seguida, são simuladas 36 novas vendas usando a função `norm.rvs()` da biblioteca SciPy, que gera valores aleatórios a partir da distribuição normal com os novos parâmetros. Finalmente, um histograma dos novos dados simulados é criado e exibido usando Matplotlib.
'''