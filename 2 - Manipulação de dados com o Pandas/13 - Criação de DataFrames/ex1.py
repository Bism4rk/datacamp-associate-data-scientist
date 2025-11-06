import pandas as pd

# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

'''
O código acima demonstra como criar um DataFrame do Pandas a partir de uma lista de dicionários. Cada dicionário na lista representa uma linha no DataFrame, com as chaves correspondendo aos nomes das colunas. Após a criação do DataFrame, ele é impresso para exibir os dados estruturados.
'''