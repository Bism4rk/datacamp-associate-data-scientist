# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

'''
O código acima demonstra como atualizar e remover elementos em um dicionário em Python. Ao alterar a capital da Alemanha de Bonn para Berlim, mostramos como modificar o valor associado a uma chave existente. Além disso, ao remover a Austrália do dicionário, ilustramos como excluir um par chave-valor. Essas operações são fundamentais para a manipulação de dicionários, permitindo que os dados sejam mantidos atualizados e relevantes conforme necessário.
'''