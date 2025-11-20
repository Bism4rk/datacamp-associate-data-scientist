import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
world_happiness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\world_happiness.csv')

# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x='grams_sugar_per_day', y='happiness_score', data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)

'''
O código acima demonstra que, apesar de haver uma correlação estatística entre a quantidade de açúcar consumida por dia e o índice de felicidade, essa correlação não implica causalidade. Fatores externos, como a economia do país ou o acesso a serviços de saúde, podem influenciar tanto o consumo de açúcar quanto o nível de felicidade, levando a uma correlação espúria. Portanto, é crucial interpretar correlações com cautela e considerar possíveis variáveis de confusão antes de tirar conclusões sobre relações causais.
'''