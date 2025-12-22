import pandas as pd
import numpy as np

used_cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\used_cars.csv')

number_of_photos = used_cars['number_of_photos'].astype('category')

print(used_cars['number_of_photos'].value_counts())

# Find the average score
average_score = used_cars["number_of_photos"].astype(int).mean()

# Print the average
print(average_score)

'''
O código acima demonstra como converter uma coluna categórica de volta para numérica em um DataFrame do pandas. Primeiro, a coluna 'number_of_photos' é convertida para o tipo categórico. Em seguida, o código calcula a média dos valores originais convertendo-os de volta para inteiros usando astype(int) e aplicando a função mean(). Finalmente, a média é impressa. Esse processo é útil quando você precisa realizar operações numéricas em dados que foram inicialmente categorizados.
'''