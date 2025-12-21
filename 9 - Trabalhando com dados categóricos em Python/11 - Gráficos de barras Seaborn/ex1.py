import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

reviews = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\reviews.csv')

# Print the frequency counts of "Period of stay"
print(reviews['Period of stay'].value_counts())

sns.set(font_scale=1.4)
sns.set_style("whitegrid")

# Create a bar plot of "Helpful votes" by "Period of stay"
sns.catplot(x="Period of stay", y="Helpful votes", data=reviews, kind='bar')
plt.show()

'''
O código acima demonstra como criar um gráfico de barras usando a biblioteca Seaborn em Python. Ele começa importando as bibliotecas necessárias: seaborn, matplotlib.pyplot e pandas. Em seguida, lê um arquivo CSV contendo dados de avaliações de viajantes. O código então imprime a contagem de frequências da coluna "Period of stay" para entender a distribuição dos dados nessa categoria. Depois, configura o estilo do gráfico, ajustando o tamanho da fonte para 1.4 e definindo o fundo como "whitegrid". Finalmente, cria um gráfico de barras que mostra a média de votos úteis recebidos por diferentes períodos de estadia e exibe o gráfico.
'''