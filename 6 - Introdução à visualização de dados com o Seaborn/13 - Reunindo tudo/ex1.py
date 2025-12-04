# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

survey_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\survey_data.csv')

# Set palette to "Blues"
sns.set_palette('Blues')

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue='Village - town')

# Set title to "Age of Those Interested in Pets vs. Not"
g.figure.suptitle('Age of Those in Villages vs. Towns', y=1.03)

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de caixa (box plot) usando a biblioteca Seaborn para comparar a distribuição de idades entre gêneros, subdivididos pela localização (vila ou cidade). A paleta de cores "Blues" é aplicada para melhorar a estética do gráfico, e um título é adicionado para contextualizar a visualização. Finalmente, o gráfico é exibido usando plt.show().
'''