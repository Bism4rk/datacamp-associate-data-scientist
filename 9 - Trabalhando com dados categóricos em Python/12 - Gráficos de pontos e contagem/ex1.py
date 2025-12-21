import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

reviews = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\reviews.csv')

# Create a point plot with catplot using "Hotel stars" and "Nr. reviews"
sns.catplot(
  # Split the data across Hotel stars and summarize Nr. reviews
  x="Hotel stars",
  y="Nr. reviews",
  data=reviews,
  # Specify a point plot
  kind="point",
  hue="Pool",
  # Make sure the lines and points don't overlap
  dodge=True
)
plt.show()

'''
O código acima demonstra como criar um gráfico de pontos usando a função catplot da biblioteca Seaborn em Python. Ele começa importando as bibliotecas necessárias: seaborn, matplotlib.pyplot e pandas. Em seguida, lê um arquivo CSV contendo dados de avaliações de hotéis. O código então cria um gráfico de pontos que exibe o número de avaliações (Nr. reviews) em relação à classificação do hotel (Hotel stars), diferenciando os pontos com base na presença ou ausência de piscina (Pool). A opção dodge=True é usada para evitar sobreposição entre os pontos e linhas correspondentes às diferentes categorias de piscina. Finalmente, o gráfico é exibido usando plt.show().
'''