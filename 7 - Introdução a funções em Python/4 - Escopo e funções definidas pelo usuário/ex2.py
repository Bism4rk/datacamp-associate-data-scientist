# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
    
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

'''
O código acima demonstra o uso da palavra-chave global para modificar uma variável global dentro de uma função. Antes de chamar a função change_team(), a variável team tem o valor "teen titans". Após a chamada da função, o valor de team é alterado para "justice league", refletindo a mudança feita dentro da função.
'''