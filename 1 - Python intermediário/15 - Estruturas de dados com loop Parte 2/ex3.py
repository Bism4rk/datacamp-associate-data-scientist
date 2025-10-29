# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper() # type: ignore
print(cars)

# Print cars
print(cars)

'''
O código acima itera sobre as linhas de um DataFrame do pandas usando o método iterrows(). Em cada iteração, ele adiciona uma nova coluna 'COUNTRY' ao DataFrame, onde o valor é a versão em maiúsculas da coluna 'country' daquela linha. Após o loop, ele imprime o DataFrame atualizado. 
'''