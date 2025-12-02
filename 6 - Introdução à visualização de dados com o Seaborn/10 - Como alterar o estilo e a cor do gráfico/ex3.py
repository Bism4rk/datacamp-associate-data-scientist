# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

survey_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\survey_data.csv')


# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
sns.set_palette(["#39A7D0", "#36ADA4"])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()

'''
O código acima demonstra como alterar o estilo e a paleta de cores de um gráfico usando a biblioteca Seaborn em Python. Primeiro, o estilo do gráfico é definido como "darkgrid", que adiciona uma grade escura ao fundo do gráfico para melhorar a legibilidade. Em seguida, uma paleta de cores personalizada é definida usando códigos hexadecimais para criar uma combinação específica de cores. Finalmente, um gráfico de caixa (box plot) é criado para visualizar a distribuição das idades dos participantes da pesquisa, categorizadas por gênero. A exibição do gráfico atualizado é realizada com a função plt.show().
'''