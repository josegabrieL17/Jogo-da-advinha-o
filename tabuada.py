#tabuada
numero = int(input('Digite a tabuada que quer: '))
multiplicador = 1 
while (multiplicador <= 10):
    resultado = numero * multiplicador
    print(f'{numero} x {multiplicador} = {resultado}')
    multiplicador = multiplicador +1