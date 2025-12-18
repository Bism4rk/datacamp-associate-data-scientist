import pandas as pd

adult = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\adult.csv')

# Create a list of user-selected variables
user_list = ["Education", "Above/Below 50k"]

# Create a GroupBy object using this list
gb = adult.groupby(by=user_list)

# Find the mean for the variable "Hours/Week" for each group - Be efficient!
print(gb['Hours/Week'].mean())

'''
O código acima demonstra como agrupar dados em um DataFrame do pandas com base em uma lista de colunas selecionadas pelo usuário. Primeiro, o conjunto de dados "adult" é carregado a partir de um arquivo CSV. Em seguida, uma lista chamada `user_list` é criada, contendo os nomes das colunas pelas quais os dados serão agrupados: "Education" e "Above/Below 50k". O método `groupby()` é então utilizado para criar um objeto GroupBy com base nessas colunas. Finalmente, o código calcula e imprime a média da coluna "Hours/Week" para cada grupo formado, permitindo uma análise eficiente dos dados categóricos selecionados.
'''