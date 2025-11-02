import pandas as pd

sales = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\4 - Estatísticas de resumo\\sales_subset.csv')


# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, 'median']))

'''
O código acima demonstra como calcular o Intervalo Interquartil (IQR) e a mediana de várias colunas em um DataFrame do Pandas. Primeiro, uma função personalizada `iqr` é definida para calcular o IQR de uma coluna. Em seguida, o código imprime o IQR da coluna 'temperature_c', seguido pelo IQR de três colunas específicas: 'temperature_c', 'fuel_price_usd_per_l' e 'unemployment'. Finalmente, o código imprime tanto o IQR quanto a mediana dessas três colunas, fornecendo uma visão estatística mais abrangente dos dados.
'''