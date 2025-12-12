import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')

# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")

# Loop through columns
for c in non_numeric.columns:
  
  # Print the number of unique values
  print(f"Number of unique values in {c} column: ", non_numeric[c].nunique())

'''
O código acima carrega um conjunto de dados sobre planos de voo e filtra as colunas que contêm dados categóricos (do tipo objeto). Em seguida, ele itera sobre essas colunas e imprime o número de valores únicos presentes em cada uma delas. Isso é útil para entender a diversidade dos dados categóricos no conjunto de dados, o que pode ajudar na análise exploratória e na preparação dos dados para modelagem.
'''