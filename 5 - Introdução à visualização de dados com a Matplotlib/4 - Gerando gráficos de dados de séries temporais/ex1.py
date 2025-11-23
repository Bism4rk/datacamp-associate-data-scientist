# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

climate_change = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\5 - Introdução à visualização de dados com a Matplotlib\\climate_change.csv', parse_dates=['date'], index_col='date')

'''
O código acima demonstra como carregar um conjunto de dados de mudanças climáticas a partir de um arquivo CSV usando a biblioteca pandas. A coluna 'date' é analisada como datas e definida como o índice do DataFrame, facilitando a manipulação e análise temporal dos dados climáticos.
'''


