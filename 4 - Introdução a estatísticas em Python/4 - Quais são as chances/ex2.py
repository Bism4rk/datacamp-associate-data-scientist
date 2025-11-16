import pandas as pd
import numpy as np

amir_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\amir_deals.csv', index_col=0)

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / amir_deals['product'].shape[0]
print(probs)



'''
O código acima demonstra como calcular a probabilidade de selecionar um negócio com cada produto específico no conjunto de dados "amir_deals". Primeiro, ele conta o número de negócios para cada produto usando `value_counts()`. Em seguida, calcula a probabilidade dividindo o número de negócios de cada produto pelo total de negócios no conjunto de dados. Finalmente, imprime as probabilidades calculadas.
'''