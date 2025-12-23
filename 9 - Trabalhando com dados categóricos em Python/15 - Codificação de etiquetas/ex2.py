import pandas as pd

used_cars_updated = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\used_cars.csv')

color_map = {1: 'other', 0: 'black', 2: 'white'}

fuel_map = {3: 'gasoline',
 2: 'gas',
 0: 'diesel',
 5: 'hybrid-petrol',
 4: 'hybrid-diesel',
 1: 'electric'}

transmission_map = {0: 'automatic', 1: 'mechanical'}


# Update the color column using the color_map
used_cars_updated["color"] = used_cars_updated['color'].map(color_map)
# Update the engine fuel column using the fuel_map
used_cars_updated["engine_fuel"] = used_cars_updated['engine_fuel'].map(fuel_map)
# Update the transmission column using the transmission_map
used_cars_updated["transmission"] = used_cars_updated['transmission'].map(transmission_map)

# Print the info statement
print(used_cars_updated.info())

'''
O código acima demonstra como substituir códigos numéricos por categorias significativas em um DataFrame do pandas. Ele lê um arquivo CSV contendo dados de carros usados e utiliza dicionários de mapeamento para atualizar as colunas "color", "engine_fuel" e "transmission" com valores categóricos legíveis. Finalmente, ele imprime as informações do DataFrame atualizado para verificar as alterações. 
'''