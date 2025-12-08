# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)

'''
O código acima demonstra como usar a função `filter()` em conjunto com uma função lambda para filtrar elementos de uma lista com base em uma condição específica. A lista `fellowship` contém nomes de personagens, e a função lambda verifica o comprimento de cada nome. Apenas os nomes com mais de 6 caracteres são mantidos na lista resultante `result_list`, que é então impressa.
'''
