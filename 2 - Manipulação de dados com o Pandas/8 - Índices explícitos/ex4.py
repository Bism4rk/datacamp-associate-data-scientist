import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')
temperatures_ind = temperatures.set_index('city')


# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=['country', 'city'], ascending=[True, False]))

'''
O código acima demonstra como ordenar um DataFrame do Pandas com um índice explícito. Primeiro, ele ordena o DataFrame 'temperatures_ind' pelos valores do índice (cidades) em ordem crescente. Em seguida, ele mostra como ordenar o DataFrame pelo nível do índice 'city'. Por fim, o código ordena o DataFrame primeiro pelo nível do índice 'country' em ordem crescente e depois pelo nível do índice 'city' em ordem decrescente. Isso ilustra a flexibilidade do Pandas na ordenação de dados com múltiplos níveis de índice.
'''