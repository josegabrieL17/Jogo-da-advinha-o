print('***********************************')
print('*Bem vindo, ao JOGO DE ADIVINHAÇÃO*')
print('***********************************')

#definindo número secreto
numeroSecreto = 38

#definindo o número de tentativas
numeroTentativas = 3

while(numeroTentativas > 0):
    numeroTentativas = numeroTentativas -1

#recebendo o chute
    chuteString = input('Digite um número: ')
    print('Você digitou o número', chuteString)
    chute = int(chuteString)

#declarando as condições
    if numeroSecreto == chute:
        print('Você acertou!')
    elif(chute>numeroSecreto):
        print("Você errou! o número é menor")
    else:
        print('Você errou! O número secreto é maior')