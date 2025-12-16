import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\salaries.csv')

# Create a bar plot of salary versus company size, factoring in employment status
sns.barplot(data=salaries, x="Company_Size", y="Salary_USD", hue="Employment_Status")
plt.show()

'''
O código acima demonstra como criar um gráfico de barras que compara os salários médios com base no tamanho da empresa, levando em consideração o status de emprego (por exemplo, tempo integral, meio período, contratado). Isso é útil para gerar hipóteses sobre como o tamanho da empresa e o tipo de emprego podem influenciar os salários dos funcionários. Por exemplo, pode-se observar que empresas maiores tendem a pagar salários mais altos para funcionários em tempo integral em comparação com empresas menores ou funcionários contratados.
'''