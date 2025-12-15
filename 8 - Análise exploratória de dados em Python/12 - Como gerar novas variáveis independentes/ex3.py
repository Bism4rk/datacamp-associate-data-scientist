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

# Create salary labels
salary_labels = ["entry", "mid", "senior", "exec"]

# Create the salary ranges list
salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]

# Create salary_level
salaries["salary_level"] = pd.cut(salaries["Salary_USD"],
                                  bins=salary_ranges,
                                  labels=salary_labels)

# Plot the count of salary levels at companies of different sizes
sns.countplot(data=salaries, x="Company_Size", hue="salary_level")
plt.show()

'''
O código acima demonstra como criar uma nova variável categórica "salary_level" com base em quartis de salários. A variável é então utilizada para visualizar a distribuição dos níveis salariais em diferentes tamanhos de empresas usando um gráfico de contagem.
'''