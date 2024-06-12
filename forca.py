def jogar_forca():

    print("**********************************************************")
    print("    BEM VINDO MEU NOBRE AO JOGO DA FORCA NESSA BAGAÇA")
    print("**********************************************************")

    
    #Definir qual a palavra secreta
    palavraSecreta = "GOJO"

    enforcou = False
    acertou = False


    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavraSecreta:
            if(chute.upper() == letra.upper):
                print("VOCÊ ENCONTROU A LETRA {} NA POSIÇÃO {} MEU NOBRE".format(chute, index))
            index = index + 1
        print("escolha outra letra")
       


    print("END GAME")
if(__name__ == "__main__"):
    jogar_forca()