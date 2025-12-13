import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])

print(divorce.dtypes)

'''
O código acima demonstra como importar um arquivo CSV contendo dados sobre divórcios, especificando quais colunas devem ser interpretadas como datas durante a importação. Isso é importante para garantir que as colunas de data sejam tratadas corretamente no DataFrame resultante, permitindo análises temporais mais precisas.
'''
