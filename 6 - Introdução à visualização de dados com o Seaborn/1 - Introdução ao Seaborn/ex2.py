from stuff import region
# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de contagem (count plot) usando a biblioteca Seaborn em Python. Primeiro, ele importa os dados necessários (região) de um módulo chamado "stuff". Em seguida, cria um gráfico de contagem com a região no eixo y, utilizando a função sns.countplot(). Finalmente, o gráfico é exibido usando a função plt.show().
'''