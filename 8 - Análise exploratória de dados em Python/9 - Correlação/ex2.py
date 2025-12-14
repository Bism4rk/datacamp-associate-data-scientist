import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

# Create the scatterplot
sns.scatterplot(x='marriage_duration', y='num_kids', data=divorce)
plt.show()

'''
O código acima demonstra como importar um arquivo CSV contendo dados sobre divórcios e criar um gráfico de dispersão (scatterplot) para visualizar a relação entre a duração do casamento (marriage_duration) e o número de filhos (num_kids). Isso ajuda a identificar possíveis correlações entre essas duas variáveis.
'''