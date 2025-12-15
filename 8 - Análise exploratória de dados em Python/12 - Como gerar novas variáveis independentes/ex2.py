import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\salaries.csv')

# Find the 25th percentile
twenty_fifth = salaries["Salary_USD"].quantile(0.25)

# Save the median
salaries_median = salaries["Salary_USD"].median()

# Gather the 75th percentile
seventy_fifth = salaries["Salary_USD"].quantile(0.75)
print(twenty_fifth, salaries_median, seventy_fifth)

'''
O código acima demonstra como calcular percentis específicos (25º e 75º) e a mediana de uma variável numérica em um DataFrame do pandas. No exemplo, a variável "Salary_USD" é analisada para obter esses valores estatísticos, que são úteis para entender a distribuição dos salários na amostra de dados. O 25º percentil indica o valor abaixo do qual 25% dos salários estão localizados, enquanto o 75º percentil indica o valor abaixo do qual 75% dos salários estão localizados. A mediana representa o valor central da distribuição dos salários, fornecendo uma medida robusta de tendência central que não é afetada por valores extremos.
'''