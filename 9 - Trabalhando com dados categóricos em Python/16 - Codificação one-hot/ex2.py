import pandas as pd

used_cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\used_cars.csv')

# Create one-hot encoding for just two columns
used_cars_simple = pd.get_dummies(
  used_cars,
  # Specify the columns from the instructions
  columns=['manufacturer_name', 'transmission'],
  # Set the prefix
  prefix='dummy'
)

# Print the shape of the new dataset
print(used_cars_simple.shape)

'''
O código acima demonstra como realizar a codificação one-hot em um conjunto de dados de carros usados usando a biblioteca pandas em Python. Ele lê um arquivo CSV contendo os dados dos carros e aplica a função `pd.get_dummies()` para criar variáveis dummy (one-hot encoding) para as colunas "manufacturer_name" e "transmission". O prefixo 'dummy' é adicionado aos nomes das novas colunas criadas. Finalmente, o código imprime a forma (número de linhas e colunas) do novo conjunto de dados resultante após a codificação. A codificação one-hot é uma técnica útil para converter variáveis categóricas em um formato que pode ser facilmente utilizado em modelos de machine learning.
'''