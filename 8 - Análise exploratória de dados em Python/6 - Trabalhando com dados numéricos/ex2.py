import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')


# Price standard deviation by Airline
planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())

print(planes[["Airline", "airline_price_st_dev"]].value_counts())

# Median Duration by Airline
planes["airline_median_duration"] = planes.groupby("Airline")["Duration"].transform(lambda x: x.median())

print(planes[["Airline","airline_median_duration"]].value_counts())

# Mean Price by Destination
planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(lambda x: x.mean())

print(planes[["Destination","price_destination_mean"]].value_counts())

'''
O código acima demonstra como calcular estatísticas agregadas, como desvio padrão, mediana e média, para diferentes grupos em um conjunto de dados de voos. Utilizando o método `groupby` do pandas, o código agrupa os dados por "Airline" e "Destination" e aplica funções de agregação para calcular o desvio padrão dos preços por companhia aérea, a mediana da duração dos voos por companhia aérea e a média dos preços por destino. Essas estatísticas são então adicionadas como novas colunas ao DataFrame original, permitindo uma análise mais aprofundada dos dados agrupados.
'''