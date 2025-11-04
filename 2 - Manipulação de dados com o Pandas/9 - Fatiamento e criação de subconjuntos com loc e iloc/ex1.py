import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')
temperatures_ind = temperatures.set_index('city')

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc['Pakistan':'Philippines'])

# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc['Lahore':'Manila'])

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Philippines', 'Manila')])

'''
O código acima demonstra como fatiar um DataFrame do Pandas com um índice explícito usando o método loc. Primeiro, o código ordena o DataFrame 'temperatures_ind' pelos valores do índice e armazena o resultado em 'temperatures_srt'. Em seguida, ele mostra como fatiar o DataFrame para obter todas as linhas entre 'Pakistan' e 'Philippines'. Depois, tenta fatiar entre 'Lahore' e 'Manila', mas isso não funciona corretamente porque esses valores não são níveis do índice. Finalmente, o código realiza um fatiamento correto usando tuplas para especificar tanto o país quanto a cidade, obtendo todas as linhas entre ('Pakistan', 'Lahore') e ('Phil
'''