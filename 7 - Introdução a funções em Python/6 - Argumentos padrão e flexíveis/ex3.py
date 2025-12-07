# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)

'''
O código acima demonstra como definir uma função em Python que aceita um número variável de argumentos posicionais usando `*args`. A função `gibberish` concatena todas as strings passadas como argumentos e retorna a string resultante. Ela é chamada duas vezes: uma vez com um único argumento e outra vez com vários argumentos, mostrando a flexibilidade do uso de `*args`.
'''