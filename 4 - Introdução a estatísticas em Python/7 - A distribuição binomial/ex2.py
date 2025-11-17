# Import binom from scipy.stats
from scipy.stats import binom

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, 0.3)

print(prob_3)

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)

print(prob_less_than_or_equal_1)

# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)

print(prob_greater_than_1)

'''
O código acima demonstra o uso da distribuição binomial para calcular probabilidades específicas relacionadas ao fechamento de negócios. Primeiro, calcula a probabilidade de fechar exatamente 3 de 3 negócios. Em seguida, calcula a probabilidade de fechar 1 ou menos negócios e, finalmente, calcula a probabilidade de fechar mais de 1 negócio. As probabilidades são então impressas.
'''