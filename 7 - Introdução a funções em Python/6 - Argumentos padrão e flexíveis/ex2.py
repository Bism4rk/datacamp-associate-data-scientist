# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", echo=5, intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)

'''
O código acima demonstra como definir uma função em Python com múltiplos argumentos padrão e como usar esses argumentos para modificar o comportamento da função. A função `shout_echo` recebe uma string `word1`, um argumento opcional `echo` que determina quantas vezes a string deve ser repetida, e um argumento booleano `intense` que, se verdadeiro, converte a string repetida para maiúsculas antes de adicionar três pontos de exclamação no final.
'''