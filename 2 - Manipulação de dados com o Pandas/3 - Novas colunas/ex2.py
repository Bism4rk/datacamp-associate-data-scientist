import pandas as pd

homelessness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\2 - Classificação e criação de subconjuntos\\homelessness.csv')

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop'] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)

'''
O código acima demonstra como criar uma nova coluna em um DataFrame do Pandas que calcula o número de indivíduos em situação de rua por 10.000 habitantes da população estadual. Em seguida, ele filtra as linhas do DataFrame para incluir apenas os estados onde essa proporção é maior que 20. Depois, o DataFrame filtrado é ordenado em ordem decrescente com base na nova coluna "indiv_per_10k". Finalmente, o código seleciona apenas as colunas "state" e "indiv_per_10k" do DataFrame ordenado e imprime o resultado para visualização.
'''