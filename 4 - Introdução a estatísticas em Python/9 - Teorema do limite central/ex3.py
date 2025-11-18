import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amir_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\amir_deals.csv', index_col=0)
all_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\all_deals.csv', index_col=0) # Not actual file, just here as placeholder

# Set seed to 321
np.random.seed(321)

sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20, replace=True)
  # Take mean of cur_sample
  cur_mean = np.mean(cur_sample)
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals['num_users']))

'''
O código acima utiliza o Teorema do Limite Central para comparar a média das médias amostrais de uma variável 'num_users' da base de dados 'all_deals' com a média real da mesma variável na base de dados 'amir_deals'. Primeiro, uma semente aleatória é definida para garantir a reprodutibilidade dos resultados. Em seguida, são realizadas 30 amostras aleatórias de tamanho 20 da variável 'num_users' da base 'all_deals', calculando a média de cada amostra e armazenando essas médias em uma lista. Finalmente, o código imprime a média das médias amostrais e a média real da variável 'num_users' na base 'amir_deals', permitindo a comparação entre as duas médias.
'''