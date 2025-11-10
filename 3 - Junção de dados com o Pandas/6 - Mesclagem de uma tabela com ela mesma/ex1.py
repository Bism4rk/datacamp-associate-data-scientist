import pandas as pd

crews = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\crews.pkl')

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

'''
O código acima demonstra como mesclar uma tabela do Pandas consigo mesma para encontrar relações específicas entre os dados. No exemplo, a tabela 'crews' é mesclada com ela mesma com base na coluna 'id', permitindo identificar membros da equipe que trabalharam sob a direção de um diretor específico. A filtragem é feita para selecionar apenas as linhas onde o trabalho do diretor é 'Director' e o trabalho do membro da equipe não é 'Director'. O resultado final exibe as primeiras linhas do DataFrame resultante, mostrando essas relações.
'''