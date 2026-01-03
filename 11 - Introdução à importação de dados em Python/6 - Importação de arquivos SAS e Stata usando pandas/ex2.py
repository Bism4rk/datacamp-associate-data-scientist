# Import sas7bdat package
from sas7bdat import SAS7BDAT
import pandas as pd
import matplotlib.pyplot as plt

# Save file to a DataFrame: df_sas
with SAS7BDAT('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

'''
O código acima demonstra como importar um arquivo SAS (.sas7bdat) usando a biblioteca sas7bdat em Python. Primeiro, o arquivo é lido e convertido em um DataFrame do pandas. Em seguida, a função head() é usada para exibir as primeiras linhas do DataFrame, permitindo uma visualização rápida dos dados importados. Finalmente, um histograma da coluna 'P' do DataFrame é plotado usando matplotlib para analisar a distribuição dos valores nessa coluna.
'''