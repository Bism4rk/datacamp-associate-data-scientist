# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

survey_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\survey_data.csv')

# Set the style to "whitegrid"
sns.set_style('whitegrid')


# Create a count plot of survey responses
category_order = ["male", "female"]

sns.catplot(x="Gender", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

# Set the color palette to "Purples"
sns.set_palette('Purples')

sns.catplot(x="Gender", 
            data=survey_data, 
            kind="count", 
            order=category_order)


plt.show()

# Change the color palette to "RdBu"
sns.set_palette("RdBu")

sns.catplot(x="Gender", 
            data=survey_data, 
            kind="count", 
            order=category_order)


plt.show()

'''
O código acima demonstra como alterar o estilo e a paleta de cores de um gráfico usando a biblioteca Seaborn em Python. Primeiro, o estilo do gráfico é definido como "whitegrid", que adiciona uma grade branca ao fundo do gráfico para melhorar a legibilidade. Em seguida, um gráfico de contagem (count plot) é criado para visualizar as respostas dos pais em uma pesquisa, com as categorias ordenadas de "Never" a "Always". Em seguida, a paleta de cores do gráfico é alterada para "Purples", que aplica uma escala de tons roxos ao gráfico. Finalmente, a paleta de cores é modificada novamente para "RdBu", que utiliza uma combinação de vermelho e azul. Cada alteração de estilo e cor é seguida pela exibição do gráfico atualizado.
'''