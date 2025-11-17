# Import uniform from scipy.stats
from scipy.stats import uniform

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5, min_time, max_time)
print(prob_less_than_5)

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)
print(prob_greater_than_5)

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)
print(prob_between_10_and_20)

'''
O código acima demonstra como usar a distribuição uniforme contínua para calcular probabilidades associadas ao tempo de espera para um backup que ocorre a cada 30 minutos. Ele calcula a probabilidade de esperar menos de 5 minutos, mais de 5 minutos e entre 10 e 20 minutos, utilizando a função de distribuição acumulada (CDF) da distribuição uniforme.
'''