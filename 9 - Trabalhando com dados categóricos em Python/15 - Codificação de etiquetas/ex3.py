import pandas as pd
import numpy as np

used_cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\used_cars.csv')

# Print the "manufacturer_name" frequency table.
print(used_cars["manufacturer_name"].value_counts())

# Create a Boolean column for the most common manufacturer name
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains("Volkswagen", regex=False), 1, 0
)
  
# Check the final frequency table
print(used_cars['is_volkswagen'].value_counts())

'''
O código acima demonstra como trabalhar com dados categóricos em Python usando a biblioteca pandas. Primeiro, ele lê um arquivo CSV contendo dados de carros usados e imprime uma tabela de frequência para a coluna "manufacturer_name". Em seguida, ele cria uma nova coluna booleana chamada "is_volkswagen", que indica se o fabricante do carro é Volkswagen (1) ou não (0). Finalmente, ele imprime a tabela de frequência da nova coluna para verificar os resultados.
'''