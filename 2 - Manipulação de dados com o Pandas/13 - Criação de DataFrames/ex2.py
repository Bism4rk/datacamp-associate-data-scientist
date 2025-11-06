import pandas as pd

# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 	6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)

'''
O código acima demonstra como criar um DataFrame do Pandas a partir de um dicionário de listas. Cada chave no dicionário representa uma coluna no DataFrame, e os valores associados são listas que contêm os dados para cada linha. Após a criação do DataFrame, ele é impresso para exibir os dados estruturados.
'''