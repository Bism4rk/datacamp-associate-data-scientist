# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france'])

# Create sub-dictionary data
data = {
    'capital': 'rome',
    'population': 59.83
}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

'''
O código acima demonstra como criar um dicionário de dicionários em Python, onde cada país é uma chave que mapeia para outro dicionário contendo informações detalhadas, como a capital e a população. Isso permite uma organização mais estruturada dos dados, facilitando o acesso e a manipulação das informações relacionadas a cada país. Ao adicionar a Itália com seus respectivos dados ao dicionário "europe", podemos expandir facilmente nosso conjunto de dados de maneira clara e eficiente.
'''