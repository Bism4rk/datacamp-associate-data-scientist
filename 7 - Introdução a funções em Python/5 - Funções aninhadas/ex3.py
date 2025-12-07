# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word + word
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + "!!!"
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')

'''
O código acima demonstra o uso da palavra-chave `nonlocal` em Python para modificar uma variável em um escopo de função externo. A função `echo_shout` recebe uma palavra, duplica-a e a imprime. Em seguida, define uma função interna `shout` que modifica a variável `echo_word` do escopo externo, adicionando '!!!' ao final. Após chamar `shout`, a função `echo_shout` imprime o valor modificado de `echo_word`. Quando chamamos `echo_shout('hello')`, o resultado é a impressão de 'hellohello' seguido de 'hellohello!!!'.
'''