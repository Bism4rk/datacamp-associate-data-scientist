# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)

'''
O código acima demonstra o uso da instrução raise em Python para lançar uma exceção personalizada. A função shout_echo verifica se o argumento echo é negativo e, se for, lança um ValueError com uma mensagem apropriada. Isso ajuda a garantir que a função seja usada corretamente, evitando comportamentos inesperados.
'''