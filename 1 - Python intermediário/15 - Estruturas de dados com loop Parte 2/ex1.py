# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

'''
O código acima demonstra como iterar sobre as linhas de um DataFrame do pandas usando o método iterrows(). Cada iteração retorna um rótulo (lab) e uma série (row) correspondente à linha do DataFrame. 
'''