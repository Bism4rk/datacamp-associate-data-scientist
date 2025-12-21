import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

reviews = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\reviews.csv')

sns.set(font_scale=1.4)
sns.set_style("darkgrid")

# Create a catplot that will count the frequency of "Score" across "Traveler type"
sns.catplot(
  x="Score", data=reviews, hue="Traveler type", kind="count"
)
plt.show()

'''
O código acima demonstra como criar um gráfico de contagem usando a função catplot da biblioteca Seaborn em Python. Ele começa importando as bibliotecas necessárias: seaborn, matplotlib.pyplot e pandas. Em seguida, lê um arquivo CSV contendo dados de avaliações de viajantes. O código então configura o estilo do gráfico, ajustando o tamanho da fonte para 1.4 e definindo o fundo como "darkgrid". Finalmente, cria um gráfico de contagem que exibe a frequência das avaliações (Score) diferenciadas pelo tipo de viajante (Traveler type) e exibe o gráfico.
'''