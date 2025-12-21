import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

reviews = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\reviews.csv')

# Set style
sns.set(font_scale=.9)
sns.set_style("whitegrid")

# Print the frequency counts for "User continent"
print(reviews["User continent"].value_counts())

# Convert "User continent" to a categorical variable
reviews["User continent"] = reviews["User continent"].astype("category")

# Reorder "User continent" using continent_categories and rerun the graphic
continent_categories = list(reviews["User continent"].value_counts().index)
reviews["User continent"] = reviews["User continent"].cat.reorder_categories(new_categories=continent_categories)
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar")
plt.show()

'''
O código acima demonstra como criar um gráfico de barras usando a biblioteca Seaborn em Python, com foco na manipulação de variáveis categóricas. Ele começa importando as bibliotecas necessárias: seaborn, matplotlib.pyplot e pandas. Em seguida, lê um arquivo CSV contendo dados de avaliações de viajantes. O código então imprime a contagem de frequências da coluna "User continent" para entender a distribuição dos dados nessa categoria. Depois, converte a coluna "User continent" em uma variável categórica e reordena suas categorias com base na frequência de ocorrência. Finalmente, cria um gráfico de barras que mostra a média das pontuações recebidas por usuários de diferentes continentes e exibe o gráfico.
'''