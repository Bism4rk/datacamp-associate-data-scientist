import pandas as pd

homelessness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\2 - Classificação e criação de subconjuntos\\homelessness.csv')

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)

'''
O código acima demonstra como filtrar um DataFrame do Pandas com base em uma lista de valores específicos. Primeiro, ele importa a biblioteca Pandas e lê um arquivo CSV contendo dados sobre pessoas em situação de rua. Em seguida, ele define uma lista chamada "canu" que contém os nomes dos estados do Deserto de Mojave. O código então cria um subconjunto do DataFrame original, filtrando apenas as linhas onde o estado está presente na lista "canu". Finalmente, o subconjunto resultante é impresso para visualização.
'''