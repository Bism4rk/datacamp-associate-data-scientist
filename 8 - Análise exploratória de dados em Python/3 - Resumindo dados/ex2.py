import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

unemployment = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\clean_unemployment.csv')

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021=('2021', 'mean'),
    # Create the std_rate_2021 column
    std_rate_2021=('2021', 'std')
)
print(continent_summary)

'''
O código acima demonstra como agrupar dados por uma categoria específica (neste caso, continente) e calcular estatísticas descritivas, como média e desvio padrão, para um ano específico (2021). Isso ajuda a entender as diferenças regionais nas taxas de desemprego.
'''