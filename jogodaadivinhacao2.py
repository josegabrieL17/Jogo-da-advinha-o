print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

# Definindo número secreto
numeroSecreto = 38

# Definindo número de tentativas 
numeroTentativas = 3

for rodada in range(1, numeroTentativas + 1):
    print("Tentativa {} de {}".format(rodada, numeroTentativas))
    chuteString = input('Digite um número: ')
    print('Você digitou o número', chuteString)
    chute = int(chuteString)

    # Verificando se o chute está correto
    if numeroSecreto == chute:
        print('Você acertou!')
        break
    elif chute > numeroSecreto:
        print("Você errou! O número é menor")
    else:
        print('Você errou! O número secreto é maior')
else:
    print("Fim de jogo, você perdeu")
    print("O número secreto era:", numeroSecreto)
    print('***********************************')