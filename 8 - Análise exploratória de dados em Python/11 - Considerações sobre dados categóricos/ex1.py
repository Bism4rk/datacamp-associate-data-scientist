import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\salaries.csv')

# Print the relative frequency of Job_Category
print(salaries['Job_Category'].value_counts(normalize=True))

'''
O código acima demonstra como calcular e exibir a frequência relativa de categorias em uma coluna categórica de um DataFrame do pandas. A função `value_counts(normalize=True)` é utilizada para obter a proporção de cada categoria em relação ao total de entradas na coluna 'Job_Category'. Isso é útil para entender a distribuição das categorias dentro do conjunto de dados.
'''