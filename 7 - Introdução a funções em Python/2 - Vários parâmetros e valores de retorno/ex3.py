# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    """Return a tuple of strings"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'    
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)

'''
O código acima demonstra como definir uma função em Python que aceita múltiplos parâmetros, concatena strings com um sufixo específico e retorna uma tupla contendo os resultados. A função `shout_all` recebe duas palavras, adiciona três pontos de exclamação a cada uma e as combina em uma tupla, que é então retornada. Finalmente, a função é chamada com os argumentos 'congratulations' e 'you', e os resultados são desempacotados em `yell1` e `yell2`, que são impressos individualmente.
'''