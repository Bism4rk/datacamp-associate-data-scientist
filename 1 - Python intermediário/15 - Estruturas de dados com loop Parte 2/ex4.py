# Import cars data
import pandas as pd
cars = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\1 - Python intermediário\\cars.csv', index_col=0)

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)

'''
O código acima melhora sobre a abordagem de loop para adicionar uma nova coluna 'COUNTRY' ao DataFrame, utilizando o método .apply() do pandas. Ele aplica a função str.upper a cada elemento da coluna 'country', convertendo os nomes dos países para maiúsculas, e atribui o resultado à nova coluna 'COUNTRY'. Esse método é mais eficiente e conciso do que iterar sobre as linhas do DataFrame.
'''