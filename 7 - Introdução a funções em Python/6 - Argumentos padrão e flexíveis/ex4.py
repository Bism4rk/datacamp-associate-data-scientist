# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")

'''
O código acima demonstra como definir uma função em Python que aceita um número variável de argumentos nomeados usando `**kwargs`. A função `report_status` imprime o status de um personagem de filme, iterando sobre os pares chave-valor fornecidos como argumentos nomeados e exibindo-os formatados. Ela é chamada duas vezes com diferentes conjuntos de informações sobre personagens.
'''