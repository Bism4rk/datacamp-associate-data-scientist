import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

# Define the marriage_year column
divorce["marriage_year"] = divorce["marriage_date"].dt.year # type: ignore

# Create a line plot showing the average number of kids by year
sns.lineplot(x="marriage_year", y="num_kids", data=divorce)
plt.show()

'''
O código acima importa um arquivo CSV contendo dados sobre divórcios, converte a coluna de datas de casamento para o formato DateTime e extrai o ano do casamento para uma nova coluna chamada "marriage_year". Em seguida, cria um gráfico de linha que mostra a média do número de filhos por ano de casamento, permitindo a visualização de tendências ao longo do tempo.
'''