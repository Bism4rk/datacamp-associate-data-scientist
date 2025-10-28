# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))

'''
O código acima melhora a iteração sobre a lista de áreas usando a função enumerate() para obter tanto o índice quanto o valor de cada elemento. Ele imprime o número do cômodo (começando de 1) junto com sua área correspondente.
'''