# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spell = map(lambda spell: spell + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spell)

# Print the result
print(shout_spells_list)

'''
O código acima demonstra como usar a função `map()` em conjunto com uma função lambda para modificar cada elemento de uma lista. A lista `spells` contém várias strings, e a função lambda adiciona três pontos de exclamação ('!!!') ao final de cada string. O resultado é convertido em uma lista chamada `shout_spells_list`, que é então impressa, mostrando as strings modificadas.
'''