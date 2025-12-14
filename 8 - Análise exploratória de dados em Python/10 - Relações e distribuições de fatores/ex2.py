import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

# Create the KDE plot
sns.kdeplot(x='marriage_duration', hue='num_kids', data=divorce)
plt.show()

# Update the KDE plot so that marriage duration can't be smoothed too far
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0)
plt.show()

# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative=True)
plt.show()

'''
O código acima demonstra como importar um conjunto de dados sobre divórcios e criar gráficos de densidade kernel (KDE) para visualizar a distribuição da duração do casamento, categorizada pelo número de filhos. A função `pd.read_csv` é utilizada para ler o arquivo CSV, com a opção `parse_dates` para garantir que as colunas de datas sejam interpretadas corretamente. Em seguida, a biblioteca Seaborn é empregada para gerar os gráficos KDE, onde o parâmetro `cut` é ajustado para evitar suavizações excessivas e o parâmetro `cumulative` é utilizado para exibir a função de distribuição acumulada. Essas visualizações ajudam a entender melhor como a duração do casamento varia em relação ao número de filhos.

Um KDE é uma estimativa suave da distribuição de probabilidade de uma variável contínua. Ele é útil para visualizar a forma da distribuição dos dados, identificar picos, vales e a dispersão dos valores, proporcionando insights sobre a densidade dos dados ao longo do intervalo analisado.
'''