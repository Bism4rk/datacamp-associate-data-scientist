# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + "!!!"

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)

'''
O código acima demonstra como definir uma função em Python que aceita um parâmetro e retorna um valor. A função `shout` recebe uma palavra como argumento, concatena essa palavra com três pontos de exclamação e retorna o resultado. Ao chamar a função com a string "congratulations" e armazenar o resultado na variável `yell`, a mensagem "congratulations!!!" é exibida na tela quando `yell` é impresso.
'''