import numpy as np
import matplotlib.pyplot as plt

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()

'''
O código acima simula 1000 tempos de espera para um backup que ocorre a cada 30 minutos, utilizando a distribuição uniforme contínua. Em seguida, ele cria um histograma para visualizar a distribuição dos tempos de espera simulados. 
'''
