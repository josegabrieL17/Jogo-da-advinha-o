# Sequências de escape ANSI para cores
class cor:
    RESET = '\033[0m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    ROXO = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'

print(cor.VERMELHO + 'Texto vermelho' + cor.RESET)
print(cor.VERDE + 'Texto verde' + cor.RESET)
print(cor.AZUL + 'Texto azul' + cor.RESET)
