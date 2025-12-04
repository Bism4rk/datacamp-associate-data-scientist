# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
survey_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\survey_data.csv')

# Set the figure style to "dark"
sns.set_style('dark')

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Techno", 
                data=survey_data, kind="bar",
                col='Gender')

# Add title and axis labels
g.figure.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de barras usando a biblioteca Seaborn para comparar a porcentagem de jovens que gostam de música techno, subdivididos por gênero e local de residência (vila ou cidade). O estilo da figura é definido como "dark" para melhorar a estética do gráfico, e títulos e rótulos dos eixos são adicionados para contextualizar a visualização. Finalmente, o gráfico é exibido usando plt.show().
'''