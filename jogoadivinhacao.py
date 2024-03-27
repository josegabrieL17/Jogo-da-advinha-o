import random;

print('***********************************')
print('*Bem vindo, ao JOGO DA ADIVINHAÇÃO*')
print('***********************************')


#definindo número secreto
numeroSecreto = round(random.random()*100)

#definindo o número de tentativas
numeroTentativas = 5
rodada = 1

while(rodada <= numeroTentativas):
    print('Tentativas' ,rodada,'de' ,numeroTentativas, "Digite um número entre 1-100")
    numeroTentativas = numeroTentativas -1
    print(numeroSecreto)

#recebendo o chute
    chuteString = input('Digite um número: ')
    chute = int(chuteString)

#declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print("Você errou! o número é menor")
    else:
        print('Você errou! O número secreto é maior')
    rodada = rodada +1