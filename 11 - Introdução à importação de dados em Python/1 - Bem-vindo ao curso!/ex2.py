# Read & print the first 3 lines

with open('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\moby_dick.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

'''
O código acima demonstra como ler e imprimir as três primeiras linhas de um arquivo de texto. O `with` statement garante que o arquivo seja fechado automaticamente após a leitura, mesmo se ocorrerem erros durante o processo.
'''