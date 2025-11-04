import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')
temperatures_srt = temperatures.set_index(['country', 'city']).sort_index()

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c'])

'''
O código acima demonstra como fatiar um DataFrame do Pandas com um índice explícito de múltiplos níveis usando o método loc. Primeiro, o código ordena o DataFrame 'temperatures' pelos valores dos índices 'country' e 'city', armazenando o resultado em 'temperatures_srt'. Em seguida, ele mostra como fatiar o DataFrame para obter todas as linhas entre ('India', 'Hyderabad') e ('Iraq', 'Baghdad'). Depois, ele ilustra como fatiar as colunas do DataFrame, selecionando todas as linhas mas apenas as colunas entre 'date' e 'avg_temp_c'. Finalmente, o código realiza um fatiamento combinado, obtendo tanto as linhas entre ('India', 'Hyderabad') e ('Iraq', 'Baghdad') quanto as colunas entre 'date' e 'avg_temp_c'.
'''