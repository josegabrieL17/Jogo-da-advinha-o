import forca
import jogoadivinhacao
print("**************************")
print("****Escolha seu jogo******")
print("**************************")

print("(1)Forca (2)Jogo da advinhação")

jogo = int(input("Qual jogo?: "))

if(jogo == 1):
    print("Você escolheu forca!")
    forca.jogar_forca()
else:
    print("Você escolheu o Jogo da advinhação!")
    jogoadivinhacao.jogar_adivinhacao()


