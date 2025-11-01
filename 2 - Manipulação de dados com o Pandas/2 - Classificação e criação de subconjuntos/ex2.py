import pandas as pd

homelessness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\2 - Classificação e criação de subconjuntos\\homelessness.csv')

# Select the individuals column
individuals = homelessness['individuals']

print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[['state', 'family_members']]

print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals', 'state']]

print(ind_state.head())

'''
O código acima demonstra como selecionar colunas específicas de um DataFrame do Pandas. Primeiro, ele seleciona a coluna 'individuals' e imprime as primeiras linhas. Em seguida, seleciona as colunas 'state' e 'family_members' e imprime as primeiras linhas. Por fim, seleciona as colunas 'individuals' e 'state' em uma ordem específica e imprime as primeiras linhas.
'''
