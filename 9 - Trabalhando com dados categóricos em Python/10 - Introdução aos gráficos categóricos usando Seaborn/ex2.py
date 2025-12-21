import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

reviews = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\reviews.csv')

# Set the font size to 1.25
sns.set(font_scale = 1.25)

# Set the background to "darkgrid"
sns.set_style('darkgrid')

# Create a boxplot
sns.catplot(x="Traveler type", y="Helpful votes", data=reviews, kind='box')

plt.show()

'''
O código acima demonstra como criar um boxplot usando a biblioteca Seaborn em Python. Ele começa importando as bibliotecas necessárias: seaborn, matplotlib.pyplot e pandas. Em seguida, lê um arquivo CSV contendo dados de avaliações de viajantes. Depois, configura o estilo do gráfico, ajustando o tamanho da fonte para 1.25 e definindo o fundo como "darkgrid". Finalmente, cria um boxplot que mostra a distribuição dos votos úteis recebidos por diferentes tipos de viajantes e exibe o gráfico.
'''