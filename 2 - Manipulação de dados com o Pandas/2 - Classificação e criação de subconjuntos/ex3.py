import pandas as pd

homelessness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\2 - Classificação e criação de subconjuntos\\homelessness.csv')

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == 'Mountain']

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)

'''
O código acima demonstra como filtrar um DataFrame do Pandas com base em múltiplas condições. Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV contendo dados sobre pessoas em situação de rua. Em seguida, ele cria três subconjuntos do DataFrame original: um com indivíduos onde o número é maior que 10.000, outro com regiões montanhosas, e um terceiro com membros da família menores que 1.000 na região do Pacífico. Cada subconjunto é então impresso para visualização.
'''