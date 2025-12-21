import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

reviews = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\reviews.csv')

# Add a second category to split the data on: "Free internet"
sns.set(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x="Casino", y="Score", data=reviews, kind="bar", hue="Free internet")
plt.show()

# Switch the x and hue categories
sns.set(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x="Free internet", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

# Update x to be "User continent"
sns.set(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

# Lower the font size so that all text fits on the screen.
sns.set(font_scale=1)
sns.set_style("darkgrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

'''
O código acima demonstra como criar gráficos de barras usando a biblioteca Seaborn em Python,
explorando diferentes categorias para segmentar os dados. Inicialmente, o gráfico de barras é criado
com "Casino" no eixo x e "Free internet" como a categoria de divisão. Em seguida, as categorias são invertidas,
colocando "Free internet" no eixo x e "Casino" como a categoria de divisão. Finalmente, o eixo x é alterado para "User continent", mostrando como ajustar o tamanho da fonte para garantir que todo o texto caiba na tela
'''
