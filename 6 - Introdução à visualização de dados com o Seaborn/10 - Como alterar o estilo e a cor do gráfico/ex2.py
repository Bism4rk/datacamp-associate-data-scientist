# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

survey_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\survey_data.csv')

# Set the context to "paper"
sns.set_context('paper')

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "notebook"
sns.set_context("notebook")

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "talk"
sns.set_context("talk")

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()

'''
O código acima demonstra como alterar o contexto de um gráfico usando a biblioteca Seaborn em Python. O contexto define o tamanho e a escala dos elementos do gráfico, tornando-os adequados para diferentes tipos de apresentações. O código começa definindo o contexto para "paper", que é ideal para gráficos em artigos científicos, e cria um gráfico de barras para visualizar a relação entre o número de irmãos e a solidão. Em seguida, o contexto é alterado para "notebook", adequado para visualizações em notebooks interativos, e o gráfico é recriado. O processo é repetido para os contextos "talk" e "poster", que são apropriados para apresentações orais e pôsteres, respectivamente. Cada alteração de contexto é seguida pela exibição do gráfico atualizado.
'''