# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)

'''
O código acima demonstra como definir uma função em Python que aceita múltiplos parâmetros, concatena strings com um sufixo específico e retorna o resultado. A função `shout` recebe duas palavras, adiciona três pontos de exclamação a cada uma e as combina em uma única string, que é então retornada. Finalmente, a função é chamada com os argumentos 'congratulations' e 'you', e o resultado é impresso.
'''