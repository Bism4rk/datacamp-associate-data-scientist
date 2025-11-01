import pandas as pd

homelessness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\2 - Classificação e criação de subconjuntos\\homelessness.csv')

# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)

print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())

'''
O código acima demonstra como classificar um DataFrame do Pandas com base em uma ou mais colunas. Primeiro, ele classifica os dados pelo número de indivíduos sem-teto em ordem crescente. Em seguida, classifica os dados pelo número de membros da família sem-teto em ordem decrescente. Por fim, ele classifica os dados primeiro pela região e depois pelo número de membros da família em ordem decrescente dentro de cada região.
'''