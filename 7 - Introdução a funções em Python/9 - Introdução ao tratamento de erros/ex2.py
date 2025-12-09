# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words = ""

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator") # type: ignore // this will raise an exception

'''
O código acima demonstra o uso de tratamento de erros em Python. A função shout_echo tenta concatenar múltiplas cópias de uma palavra seguida de exclamações. Se os argumentos fornecidos não forem do tipo esperado (string para word1 e inteiro para echo), a exceção é capturada, e uma mensagem de erro é exibida, evitando que o programa quebre.
'''