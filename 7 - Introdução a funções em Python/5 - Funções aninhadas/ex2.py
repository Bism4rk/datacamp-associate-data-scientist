# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

'''
O código acima demonstra o conceito de funções aninhadas e closures em Python. A função externa `echo` recebe um número `n` e define uma função interna `inner_echo` que concatena uma palavra `word1` `n` vezes. A função externa retorna a função interna, permitindo que ela retenha o valor de `n` mesmo após a execução de `echo`. Quando chamamos `echo(2)`, obtemos uma função que duplica a palavra, e quando chamamos `echo(3)`, obtemos uma função que triplica a palavra. As chamadas subsequentes a essas funções com a palavra 'hello' resultam em 'hellohello' e 'hellohellohello', respectivamente.
'''