import pandas as pd
import numpy as np

amir_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\amir_deals.csv', index_col=0)

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)

'''
O código acima demonstra a diferença entre amostragem sem e com substituição em Python. Ele utiliza o método `sample()` do pandas para selecionar 5 negócios do conjunto de dados "amir_deals". Na primeira amostragem, os negócios são selecionados sem substituição, o que significa que cada negócio só pode ser escolhido uma vez. Na segunda amostragem, os negócios são selecionados com substituição, permitindo que o mesmo negócio seja escolhido múltiplas vezes. As amostras resultantes são então impressas para comparação.
'''