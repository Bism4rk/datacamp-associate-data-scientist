# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
      offset -= 1
    else : 
      offset += 1    
    print(offset)

'''
O código acima combina um loop while com uma estrutura condicional if-else para ajustar o valor da variável `offset` em direção a zero. Começando com `offset` definido como -6, o loop continua enquanto `offset` for diferente de 0. Dentro do loop, ele imprime "correcting...", verifica se `offset` é maior que 0 para decidir se deve diminuir ou aumentar seu valor em 1, e então imprime o novo valor de `offset`. O loop termina quando `offset` atinge 0.
'''