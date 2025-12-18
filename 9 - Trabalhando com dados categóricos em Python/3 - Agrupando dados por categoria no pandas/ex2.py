import pandas as pd

adult = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\adult.csv')

# Group the adult dataset by "Sex" and "Above/Below 50k"
gb = adult.groupby(by=["Sex", "Above/Below 50k"])

# Print out how many rows are in each created group
print(gb.size())

# Print out the mean of each group for all columns
print(gb.mean(numeric_only=True))

'''
O código acima demonstra como agrupar dados em um DataFrame do pandas com base em múltiplas colunas categóricas. Primeiro, o conjunto de dados "adult" é agrupado pelas colunas "Sex" e "Above/Below 50k" usando o método `groupby()`. Em seguida, o código imprime o tamanho de cada grupo criado, mostrando quantas linhas pertencem a cada combinação única dessas categorias. Finalmente, o código calcula e imprime a média de todas as colunas numéricas para cada grupo, permitindo uma análise comparativa entre os diferentes grupos categóricos.
'''