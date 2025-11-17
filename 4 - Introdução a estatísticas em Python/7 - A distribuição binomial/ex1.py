# Import binom from scipy.stats
from scipy.stats import binom
import numpy as np

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))

# Simulate 1 week of 3 deals
print(binom.rvs(3, 0.3, size=1))

# Import binom from scipy.stats
from scipy.stats import binom

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)

# Print mean deals won per week
print(deals.mean()) # type: ignore

'''
O código acima demonstra a simulação de resultados de negócios usando a distribuição binomial. Primeiro, ele simula o resultado de um único negócio, depois simula os resultados de três negócios em uma semana e, finalmente, simula os resultados de três negócios ao longo de 52 semanas. A média dos negócios ganhos por semana é então calculada e impressa.
'''