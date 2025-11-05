import pandas as pd

temperatures = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\8 - Índices explícitos\\temperatures.csv')

# test thing to avoid errors, not actually part of exercise
temperatures['date'] = pd.to_datetime(temperatures['date'])

# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=['country', 'city'], columns="year")

# See the result
print(temp_by_country_city_vs_year)

'''
O código acima demonstra como criar uma tabela dinâmica (pivot table) usando o Pandas. Primeiro, ele adiciona uma nova coluna 'year' ao DataFrame 'temperatures', extraindo o ano da coluna 'date'. Em seguida, ele cria uma tabela dinâmica que organiza as temperaturas médias ('avg_temp_c') com índices compostos por 'country' e 'city', e colunas representando os anos. Finalmente, o resultado é impresso, mostrando a média das temperaturas para cada cidade em cada ano.ippines', 'Manila').
'''