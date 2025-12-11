import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')


# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to missing values of Price by Airline
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(airline_prices))

# Check for missing values
print(planes.isna().sum())

'''
O código acima demonstra como lidar com dados faltantes em uma coluna numérica, especificamente os preços dos bilhetes de avião. Primeiro, ele calcula o preço mediano dos bilhetes para cada companhia aérea agrupando os dados por "Airline". Em seguida, cria um dicionário a partir desses valores medianos. Finalmente, preenche os valores ausentes na coluna "Price" mapeando os preços medianos correspondentes às companhias aéreas, garantindo que os dados estejam mais completos para análises futuras.
'''