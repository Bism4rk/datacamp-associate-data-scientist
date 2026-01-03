import pandas as pd

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt' # não é um arquivo real, apenas um exemplo

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

'''
O código acima demonstra como tratar arquivos de dados simples com pandas, incluindo a especificação de separadores personalizados, ignorar linhas de comentários e lidar com valores ausentes. Além disso, ele mostra como visualizar a distribuição de uma variável numérica usando um histograma com matplotlib.
'''