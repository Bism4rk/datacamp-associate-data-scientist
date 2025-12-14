import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data=divorce, vars=['income_woman' , 'marriage_duration'])
plt.show()

'''
O código acima demonstra como importar um conjunto de dados sobre divórcios e criar um pairplot para visualizar a relação entre a renda da mulher e a duração do casamento. A função `pd.read_csv` é utilizada para ler o arquivo CSV, com a opção `parse_dates` para garantir que as colunas de datas sejam interpretadas corretamente. Em seguida, a biblioteca Seaborn é empregada para gerar um pairplot, que ajuda a identificar possíveis correlações entre as variáveis selecionadas. A visualização resultante pode fornecer insights sobre como a renda da mulher pode influenciar a duração do casamento.
'''