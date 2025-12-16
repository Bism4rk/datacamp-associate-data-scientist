import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\salaries.csv')

# Filter for employees in the US or GB
usa_and_gb = salaries[salaries["Employee_Location"].isin(["US", "GB"])]

# Create a barplot of salaries by location
sns.barplot(data=usa_and_gb, x="Employee_Location", y="Salary_USD")
plt.show()

'''
O código acima demonstra como filtrar um DataFrame para incluir apenas funcionários localizados nos Estados Unidos (US) ou no Reino Unido (GB) e, em seguida, criar um gráfico de barras que compara os salários médios nesses dois países. Isso é útil para gerar hipóteses sobre diferenças salariais entre esses locais. No caso, os dados sugerem que os salários nos Estados Unidos são significativamente mais altos do que no Reino Unido, o que pode levar a hipóteses sobre fatores econômicos, custo de vida ou políticas de remuneração que influenciam essas diferenças.
'''