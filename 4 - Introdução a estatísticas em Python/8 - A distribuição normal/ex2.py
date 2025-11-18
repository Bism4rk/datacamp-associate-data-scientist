import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

amir_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\amir_deals.csv', index_col=0)

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)

print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 =  norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)

print(pct_25)

'''
O código acima demonstra como calcular probabilidades e percentis usando a distribuição normal com a biblioteca SciPy em Python. As funções norm.cdf() e norm.ppf() são usadas para calcular a função de distribuição acumulada e o percentil, respectivamente. As probabilidades calculadas incluem a probabilidade de um negócio ser menor que 7500, maior que 1000 e entre 3000 e 7000. Além disso, o código calcula o valor abaixo do qual 25% dos negócios cairão.
'''
