import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

# Create the scatter plot
sns.scatterplot(x='woman_age_marriage', y='income_woman', hue='education_woman', data=divorce)
plt.show()

'''
O código acima demonstra como importar um conjunto de dados sobre divórcios e criar um gráfico de dispersão para visualizar a relação entre a idade da mulher no casamento e sua renda, categorizada pelo nível educacional. A função `pd.read_csv` é utilizada para ler o arquivo CSV, com a opção `parse_dates` para garantir que as colunas de datas sejam interpretadas corretamente. Em seguida, a biblioteca Seaborn é empregada para gerar o gráfico de dispersão, onde a cor dos pontos representa diferentes níveis educacionais da mulher. Essa visualização pode ajudar a identificar padrões ou tendências na relação entre idade, renda e educação.
'''