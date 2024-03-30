import random

print('***********************************')
print('* Bem vindo, ao JOGO DA ADIVINHAÇÃO*')
print('***********************************')

# Definindo número secreto
numeroSecreto = round(random.random() * 100)

# Definindo o número de tentativas
numeroTentativas = 5

while numeroTentativas > 0:
    print('*' * 35)  # Linha separadora
    print('Tentativas restantes:', numeroTentativas)
    print('Digite um número entre 1-100')

    # Recebendo o chute
    chuteString = input('Digite um número: ')
    chute = int(chuteString)

    # Declarando as condições
    if numeroSecreto == chute:
        print('Você acertou!')
        break
    elif chute > numeroSecreto:
        print("Você errou! O número é menor")
    else:
        print('Você errou! O número é maior')

    numeroTentativas -= 1

# Se o jogador usou todas as tentativas e não acertou
if numeroTentativas == 0:
    print('-' * 50)  # Linha separadora
    print('Suas tentativas acabaram. O número secreto era:', numeroSecreto, "Erro USB")
