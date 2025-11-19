# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
print(1 - expon.cdf(4, scale=2.5))

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))

'''
O código acima demonstra como calcular probabilidades usando a distribuição exponencial com a biblioteca SciPy em Python. Ele calcula a probabilidade de uma resposta levar menos de 1 hora, mais de 4 horas, e entre 3 e 4 horas, assumindo que o tempo médio de resposta é de 2.5 horas.
'''