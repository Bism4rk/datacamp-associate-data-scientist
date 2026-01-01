# Open a file as read-only and bind it to file
with open('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\moby_dick.txt', 'r') as file:
  	# Print it
    print(file.read())

'''
O código acima demonstra como abrir um arquivo em modo de leitura e imprimir seu conteúdo. O `with` statement garante que o arquivo seja fechado automaticamente após a leitura, mesmo se ocorrerem erros durante o processo.
'''