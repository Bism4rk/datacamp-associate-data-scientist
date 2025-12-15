import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

salaries = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\salaries.csv')

# Cross-tabulate Company_Size and Experience
print(pd.crosstab(salaries["Company_Size"], salaries["Experience"]))

# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"]))

# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"],
            values=salaries["Salary_USD"], aggfunc="mean"))

'''
O código acima demonstra como utilizar a função `pd.crosstab()` do pandas para criar tabelas de contingência que cruzam duas variáveis categóricas. As duas primeiras chamadas de `pd.crosstab()` geram tabelas que mostram a contagem de ocorrências para cada combinação das categorias das colunas especificadas. A terceira chamada utiliza os parâmetros `values` e `aggfunc` para calcular a média dos salários (`Salary_USD`) para cada combinação de `Job_Category` e `Company_Size`. Isso é útil para analisar a distribuição e as relações entre diferentes categorias em um conjunto de dados.
'''