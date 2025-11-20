import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
world_happiness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\world_happiness.csv')

# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x='gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['happiness_score'].corr(world_happiness['gdp_per_cap'])
print(cor)

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

'''
O código acima demonstra como a transformação logarítmica pode melhorar a correlação entre duas variáveis. Inicialmente, a correlação entre 'happiness_score' e 'gdp_per_cap' é calculada e visualizada, mostrando uma relação não linear. Após aplicar a transformação logarítmica em 'gdp_per_cap', a nova correlação com 'happiness_score' é recalculada e visualizada, revelando uma relação mais linear e uma correlação mais forte. Isso ilustra a importância de considerar transformações de dados ao analisar relações estatísticas.
'''