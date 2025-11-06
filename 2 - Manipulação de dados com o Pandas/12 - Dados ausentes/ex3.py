import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\11 - Visualização de dados\\avoplotto.pkl')

# test thing to avoid errors, not actually part of exercise
avocados['date'] = pd.to_datetime(avocados['date'])
avocados['year'] = avocados['date'].dt.year
avocados_2016 = avocados[avocados['year'] == 2016]


# From previous step
cols_with_missing = ["nb_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

'''
O código acima demonstra como lidar com dados ausentes em um DataFrame do Pandas, especificamente preenchendo esses valores ausentes com zeros. No exemplo, um DataFrame chamado "avocados" é carregado a partir de um arquivo pickle. Uma nova coluna "year" é adicionada ao DataFrame, extraída da coluna "date". Em seguida, um subconjunto do DataFrame é criado para o ano de 2016. O código então identifica colunas específicas que contêm valores ausentes e cria histogramas dessas colunas antes do preenchimento. Após preencher os valores ausentes com zeros usando o método `fillna(0)`, novos histogramas são gerados para as mesmas colunas, permitindo a visualização dos dados após o tratamento dos valores ausentes.
'''