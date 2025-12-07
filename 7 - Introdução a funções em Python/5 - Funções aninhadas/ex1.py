# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

'''
O código acima demonstra como definir funções aninhadas em Python. A função externa `three_shouts` recebe três palavras como argumentos e define uma função interna `inner` que adiciona '!!!' a uma palavra dada. A função externa então retorna uma tupla contendo as três palavras modificadas pela função interna. Quando chamamos `three_shouts('a', 'b', 'c')`, o resultado é a tupla ('a!!!', 'b!!!', 'c!!!').
'''

