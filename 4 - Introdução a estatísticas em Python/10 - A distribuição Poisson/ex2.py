# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_5 = poisson.pmf(5, 4)

print(prob_5)

# Probability of 5 responses
prob_coworker = poisson.pmf(5, 5.5)

print(prob_coworker)

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2, 4)

print(prob_2_or_less)

# Probability of > 10 responses
prob_over_10 = 1 - poisson.cdf(10, 4)

print(prob_over_10)


'''
O código acima demonstra como calcular probabilidades usando a distribuição de Poisson com a biblioteca SciPy em Python. Ele calcula a probabilidade de exatamente 5 respostas quando a média é 4, a probabilidade de exatamente 5 respostas quando a média é 5.5, a probabilidade de 2 ou menos respostas quando a média é 4, e a probabilidade de mais de 10 respostas quando a média é 4.
'''
