import pandas as pd

avocados = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\11 - Visualização de dados\\avoplotto.pkl')

# test thing to avoid errors, not actually part of exercise
avocados['date'] = pd.to_datetime(avocados['date'])
avocados['year'] = avocados['date'].dt.year
avocados_2016 = avocados[avocados['year'] == 2016]

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()

'''
O código acima demonstra como identificar e visualizar dados ausentes em um DataFrame do Pandas. No exemplo, um DataFrame chamado "avocados" é carregado a partir de um arquivo pickle. Uma nova coluna "year" é adicionada ao DataFrame, extraída da coluna "date". Em seguida, um subconjunto do DataFrame é criado para o ano de 2016. O código então verifica a presença de valores ausentes em cada célula do DataFrame e também verifica se há valores ausentes em cada coluna. Finalmente, um gráfico de barras é gerado para mostrar a contagem de valores ausentes por variável, utilizando a biblioteca Matplotlib para visualização.
'''