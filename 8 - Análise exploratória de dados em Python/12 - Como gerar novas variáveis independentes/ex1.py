import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\salaries.csv')

# Get the month of the response
salaries["month"] = salaries["date_of_response"].dt.month # type: ignore

# Extract the weekday of the response
salaries["weekday"] = salaries["date_of_response"].dt.weekday # type: ignore

# Create a heatmap
sns.heatmap(salaries.corr(numeric_only=True), annot=True)
plt.show()

'''
O código acima demonstra como gerar novas variáveis independentes a partir de uma variável de data existente em um DataFrame do pandas. A variável "date_of_response" é utilizada para extrair o mês e o dia da semana em que a resposta foi registrada, criando assim duas novas colunas: "month" e "weekday". Essas novas variáveis podem ser úteis para análises adicionais, como identificar padrões sazonais ou comportamentais nas respostas. Além disso, o código inclui a criação de um mapa de calor (heatmap) para visualizar as correlações entre as variáveis numéricas do DataFrame, o que pode ajudar a identificar relações importantes entre diferentes atributos dos dados.
'''