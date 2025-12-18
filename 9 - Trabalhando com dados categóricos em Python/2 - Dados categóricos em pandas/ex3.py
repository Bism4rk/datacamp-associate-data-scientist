import pandas as pd

adult = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\adult.csv')

# Check the dtypes
print(adult.dtypes)

# Create a dictionary with column names as keys and "category" as values
adult_dtypes = {
   "Workclass": "category",
   "Education": "category",
   "Relationship": "category",
   "Above/Below 50k": "category" 
}

# Read in the CSV using the dtypes parameter
adult2 = pd.read_csv(
  'C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\adult.csv',
  dtype=adult_dtypes # type: ignore[file-defined]
)
print(adult2.dtypes)

'''
O código acima demonstra como otimizar o uso de memória ao carregar um conjunto de dados em um DataFrame do pandas, especificando tipos de dados categóricos para colunas que contêm um número limitado de valores únicos. Primeiro, o código lê o arquivo CSV sem especificar tipos de dados, o que resulta em um uso de memória maior. Em seguida, ele cria um dicionário que mapeia os nomes das colunas para o tipo "category" e usa esse dicionário ao ler o CSV novamente. Isso reduz significativamente o uso de memória do DataFrame resultante, tornando-o mais eficiente para análise de dados.
'''