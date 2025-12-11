import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')

# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())

# Create a box plot of Price by Airline
sns.boxplot(data=planes, x='Airline', y='Price')

plt.show()

'''
O código acima demonstra como visualizar dados categóricos e numéricos usando um box plot. Primeiro, ele verifica os valores únicos na coluna "Additional_Info" para entender a distribuição dos dados categóricos. Em seguida, cria um box plot para comparar os preços dos bilhetes entre diferentes companhias aéreas, permitindo identificar variações e possíveis outliers nos preços. A visualização ajuda a compreender melhor a relação entre as categorias e os valores numéricos no conjunto de dados.
'''