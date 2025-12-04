# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')

# Create line plot
g = sns.lineplot(x="model_year", y="mpg", 
                 data=mpg,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year", ylabel="Average MPG")

# Show plot
plt.show()

'''
O código acima demonstra como adicionar títulos e rótulos aos eixos em um gráfico de linha usando Seaborn. Primeiro, importamos as bibliotecas necessárias e carregamos o conjunto de dados 'mpg'. Em seguida, criamos um gráfico de linha que mostra a média de milhas por galão (MPG) ao longo dos anos do modelo do carro, diferenciando os dados pela origem do carro. Finalmente, adicionamos um título ao gráfico e rótulos aos eixos x e y para melhorar a clareza da visualização antes de exibi-la.
'''