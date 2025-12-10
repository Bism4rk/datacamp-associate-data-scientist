import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype(float)
# Print the dtypes to check your work
print(unemployment.dtypes)

'''
O código acima demonstra como atualizar o tipo de dados da coluna '2019' para float em um DataFrame do pandas. Ele importa a biblioteca pandas, carrega os dados do arquivo 'clean_unemployment.csv', altera o tipo de dados da coluna '2019' usando o método astype(float) e imprime os tipos de dados das colunas para verificar a alteração.
'''