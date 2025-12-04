# Import Matplotlib and Seaborn
import seaborn as sns
import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')


# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)

'''
O código acima demonstra como identificar o tipo de um gráfico criado com o Seaborn em Python. Ele cria um gráfico de dispersão (scatter plot) que mostra a relação entre o peso (weight) e a potência (horsepower) dos veículos no conjunto de dados 'mpg'. Em seguida, o código obtém o tipo do objeto gráfico retornado pela função sns.relplot() e o imprime. Isso é útil para entender a estrutura do objeto gráfico e como ele pode ser manipulado ou personalizado posteriormente.
'''