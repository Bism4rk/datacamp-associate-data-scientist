# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')


# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.figure.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()

'''
O código acima demonstra como adicionar um título a um gráfico criado com o Seaborn em Python. Ele cria um gráfico de dispersão (scatter plot) que mostra a relação entre o peso (weight) e a potência (horsepower) dos veículos no conjunto de dados 'mpg'. Em seguida, o código adiciona o título "Car Weight vs. Horsepower" ao gráfico usando o método suptitle() do objeto figure associado ao gráfico. Finalmente, o gráfico é exibido com plt.show(). Isso é útil para fornecer contexto e informações adicionais sobre o gráfico para os espectadores.
'''