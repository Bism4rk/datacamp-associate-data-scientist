# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

'''
O código acima demonstra como definir uma função em Python que aceita um parâmetro. A função `shout` recebe uma palavra como argumento, concatena essa palavra com três pontos de exclamação e imprime o resultado. Ao chamar a função com a string "congratulations", a mensagem "congratulations!!!" é exibida na tela.
'''