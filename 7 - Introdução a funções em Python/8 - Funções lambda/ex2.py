# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)

'''
O código acima demonstra como definir e usar uma função lambda em Python. A função `echo_word` recebe dois argumentos: uma palavra (`word1`) e um número (`echo`). Ela retorna a palavra repetida o número de vezes especificado. No exemplo, a palavra 'hey' é repetida 5 vezes, resultando na saída 'heyheyheyheyhey'.
'''