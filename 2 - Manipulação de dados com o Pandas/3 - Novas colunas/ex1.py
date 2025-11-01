import pandas as pd

homelessness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\2 - Classificação e criação de subconjuntos\\homelessness.csv')

# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_homeless col as proportion of total homeless population to the state population
homelessness['p_homeless'] = homelessness['total'] / homelessness['state_pop']

# See the result
print(homelessness)

'''
O código acima demonstra como adicionar novas colunas a um DataFrame do Pandas. Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV contendo dados sobre pessoas em situação de rua. Em seguida, ele cria uma nova coluna chamada "total", que é a soma das colunas "individuals" e "family_members". Depois, ele adiciona outra coluna chamada "p_homeless", que representa a proporção da população total em situação de rua em relação à população do estado. Finalmente, o DataFrame atualizado é impresso para visualização.
'''