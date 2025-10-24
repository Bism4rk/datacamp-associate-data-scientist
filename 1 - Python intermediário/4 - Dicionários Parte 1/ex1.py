# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

'''
O código acima demonstra como encontrar o índice de um elemento em uma lista e usá-lo para acessar um elemento correspondente em outra lista. Neste caso, encontramos o índice da Alemanha na lista de países e usamos esse índice para obter a capital correspondente na lista de capitais. Porém, essa abordagem pode ser ineficiente e propensa a erros, especialmente se as listas não estiverem sincronizadas corretamente. Uma maneira mais eficaz de lidar com essa situação é usar um dicionário, que mapeia diretamente cada país à sua capital, facilitando o acesso e a manutenção dos dados, e isso será explorado em exercícios futuros.
'''