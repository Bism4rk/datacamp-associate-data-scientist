import pandas as pd

avocados = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\11 - Visualização de dados\\avoplotto.pkl')

# test thing to avoid errors, not actually part of exercise
avocados['date'] = pd.to_datetime(avocados['date'])
avocados['year'] = avocados['date'].dt.year
avocados_2016 = avocados[avocados['year'] == 2016]

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

'''
O código acima demonstra como lidar com dados ausentes em um DataFrame do Pandas. No exemplo, um DataFrame chamado "avocados" é carregado a partir de um arquivo pickle. Uma nova coluna "year" é adicionada ao DataFrame, extraída da coluna "date". Em seguida, um subconjunto do DataFrame é criado para o ano de 2016. O código então remove todas as linhas que contêm valores ausentes utilizando o método `dropna()`. Finalmente, ele verifica se ainda existem colunas com valores ausentes no DataFrame resultante, imprimindo o resultado.
'''