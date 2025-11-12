import pandas as pd

classic_18 = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\10 - Verificação de integridade\\classic_18.csv')
classic_19 = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\10 - Verificação de integridade\\classic_19.csv')
pop_18 = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\10 - Verificação de integridade\\pop_18.csv')
pop_19 = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\10 - Verificação de integridade\\pop_19.csv')

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)

'''
O código acima demonstra como utilizar a função .isin() do Pandas para filtrar um DataFrame com base em valores presentes em outro DataFrame. Ele começa carregando quatro conjuntos de dados CSV relacionados a músicas clássicas e populares de 2018 e 2019. Em seguida, concatena os dados clássicos e populares separadamente para criar dois DataFrames combinados. Depois, realiza uma junção (merge) entre os dois DataFrames combinados com base na coluna 'tid', que representa o identificador da música. Finalmente, utiliza a função .isin() para filtrar o DataFrame de músicas clássicas, mantendo apenas aquelas cujos 'tid' estão presentes no DataFrame resultante da junção, e imprime o resultado. Isso é útil para identificar quais músicas clássicas também são populares.
'''