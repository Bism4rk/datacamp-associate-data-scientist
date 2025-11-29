# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\student_data.csv')

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x='school', 
                data=student_data, hue="location", hue_order=['Rural', 'Urban'], palette=palette_colors)

# Display plot
plt.show()

'''
O código acima demonstra como criar um gráfico de contagem (count plot) usando a biblioteca Seaborn, onde os dados são subdivididos por uma terceira variável (location) representada por diferentes cores. A paleta de cores personalizada é definida por um dicionário que mapeia os valores da subgrupo para cores específicas. O gráfico resultante mostra a contagem de estudantes em cada escola, diferenciando entre localizações rurais e urbanas.
'''