import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amir_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\amir_deals.csv', index_col=0)

# Create a histogram of num_users and show
amir_deals['num_users'].hist()
plt.show()

# Set seed to 104
np.random.seed(104)

sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()

'''
O código acima ilustra o Teorema do Limite Central ao demonstrar como a distribuição das médias amostrais se aproxima de uma distribuição normal, mesmo quando a distribuição original dos dados (número de usuários) não é normal. Primeiro, um histograma da variável 'num_users' é criado para visualizar sua distribuição original. Em seguida, são realizadas 100 amostras aleatórias de tamanho 20 da variável 'num_users', calculando a média de cada amostra e armazenando essas médias em uma lista. Finalmente, um histograma das médias amostrais é plotado, mostrando que a distribuição dessas médias tende a ser normal, conforme previsto pelo Teorema do Limite Central.
'''