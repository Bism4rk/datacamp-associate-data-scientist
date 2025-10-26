# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")

'''
O código acima demonstra o uso de declarações if-elif-else para verificar múltiplas condições. Para a variável 'room', ele verifica se é "kit" ou "bed" e imprime mensagens apropriadas; caso contrário, indica que está olhando em outro lugar. Para a variável 'area', ele classifica o tamanho do local em grande, médio ou pequeno, imprimindo a mensagem correspondente.
'''