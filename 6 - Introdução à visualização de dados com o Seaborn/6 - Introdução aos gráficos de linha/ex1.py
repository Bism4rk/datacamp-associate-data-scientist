# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')

# Create line plot
sns.relplot(x="model_year", y="mpg", data=mpg, kind="line")

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de linha usando o Seaborn em Python. bla bla mais coisas aqui acabou o copilot
'''