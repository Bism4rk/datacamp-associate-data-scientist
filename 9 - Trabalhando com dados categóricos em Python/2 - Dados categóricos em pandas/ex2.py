import pandas as pd
from list import medals_won

# Create a categorical Series and specify the categories (let pandas know the order matters!)
medals = pd.Categorical(medals_won, categories=['Bronze', 'Silver', 'Gold'], ordered=True)
print(medals)

'''
O código acima cria uma Series categórica chamada "medals" a partir da lista "medals_won". As categorias são especificadas como 'Bronze', 'Silver' e 'Gold', e a ordem dessas categorias é importante, indicando que 'Bronze' é menor que 'Silver', que por sua vez é menor que 'Gold'.
'''