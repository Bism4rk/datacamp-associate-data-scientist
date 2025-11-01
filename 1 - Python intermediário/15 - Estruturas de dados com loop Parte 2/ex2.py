# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ": " + str(row['cars_per_cap']))

'''
O código acima adapta um loop para iterar sobre as linhas de um DataFrame do pandas usando o método iterrows(). Em cada iteração, ele imprime o rótulo (lab) da linha junto com o valor da coluna 'cars_per_cap' daquela linha. Ele concatena o rótulo com o valor convertido em string para exibição.
'''