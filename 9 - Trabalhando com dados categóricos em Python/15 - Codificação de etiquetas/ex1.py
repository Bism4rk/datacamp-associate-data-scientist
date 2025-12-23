import pandas as pd

used_cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\used_cars.csv')

# Convert to categorical and print the frequency table
used_cars["color"] = used_cars["color"].astype("category")
print(used_cars["color"].value_counts())

# Create a label encoding
used_cars["color_code"] = used_cars["color"].cat.codes

# Create codes and categories objects
codes = used_cars["color"].cat.codes
categories = used_cars["color"]
color_map = dict(zip(codes, categories))

# Print the map
print(color_map)

'''
O código acima demonstra como trabalhar com dados categóricos em Python usando a biblioteca pandas. Primeiro, ele lê um arquivo CSV contendo dados de carros usados e converte a coluna "color" para o tipo categórico. Em seguida, ele cria uma codificação de rótulos para as cores dos carros, atribuindo um código numérico a cada categoria de cor. Finalmente, ele cria um dicionário que mapeia esses códigos para suas respectivas categorias e imprime esse mapa.
'''