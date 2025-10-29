# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for country, capital in europe.items():
    print("the capital of " + country + " is " + capital)

'''
O código acima demonstra como iterar sobre um dicionário em Python usando o método items(). Ele imprime o nome de cada país junto com sua capital correspondente.
'''