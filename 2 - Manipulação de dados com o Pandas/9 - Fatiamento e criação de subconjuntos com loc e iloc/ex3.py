import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08-01':'2011-02-28'])

'''
O código acima demonstra duas abordagens para fatiar um DataFrame do Pandas com base em condições de data. Primeiro, ele utiliza condições booleanas para filtrar o DataFrame 'temperatures' e obter todas as linhas entre 1º de janeiro de 2010 e 31 de dezembro de 2011, armazenando o resultado em 'temperatures_bool'. Em seguida, o código define a coluna 'date' como índice do DataFrame e ordena esse índice. Finalmente, ele usa o método loc para fatiar o DataFrame ordenado 'temperatures_ind', primeiro obtendo todas as linhas entre os anos de 2010 e 2011, e depois obtendo um subconjunto mais específico entre agosto de 2010 e fevereiro de 2011.
'''