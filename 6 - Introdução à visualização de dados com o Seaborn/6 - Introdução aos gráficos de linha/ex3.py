# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower", data=mpg, kind='line', ci=None)

# Show plot
plt.show()

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style='origin', hue='origin')

# Show plot
plt.show()

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin", markers=True, dashes=False)

# Show plot
plt.show()

'''
O código acima demonstra como modificar o estilo de um gráfico gerado pelo Seaborn. slk mto foda meu olha só as opções krl meu
'''