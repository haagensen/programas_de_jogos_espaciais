"""
Os Olhos dos Monstros
versão em Python por Christian Haagensen Gontijo, 30/06/2017

Você está encurralado! Para onde quer que se volte, os olhos frios e assustadores de um monstro
do espaço o espreitam por um momento, antes que o animal se esconda atrás de uma pedra. Pouco a
pouco, os monstros se aproximam de você, tentando envolvê-lo em seus tentáculos.

Felizmente, você está com a sua pistola de prótons. Os olhos dos monstros aparecem em quatro
lugares diferentes da tela, que correspondem às teclas de 1 a 4. Se você apertar a tecla certa
enquanto os olhos do monstro estiverem na tela, ele será destruído. Existem 10 monstros... à
medida que você os destrói, sua chance de escapar aumenta.
"""
import time
import random
from colorconsole import terminal  # obrigado, Nilo! <https://github.com/lskbr/colorconsole>

screen = terminal.get_terminal(conEmu=False)

print("Os Olhos dos Monstros")

acertos = 0
tentativas = 0

for tentativas in range(11):

    time.sleep(random.randint(1, 5))

    resultado = random.randint(1, 4)
    if resultado == 1:
        linha = 5
        coluna = 1
    elif resultado == 2:
        linha = 1
        coluna = 9
    elif resultado == 3:
        linha = 5
        coluna = 18
    else:
        linha = 10
        coluna = 7
    screen.clear()
    screen.gotoXY(coluna, linha)
    print("OO")  # é, ISSO são os olhos do monstro... :-p

    tentativa = 0
    tentativaStr = input()
    if tentativaStr.upper().startswith("E"):
        break
    else:
        try:
            tentativa = int(tentativaStr)
        except:
            tentativa = 0

    if tentativa == resultado:
        acertos += 1
        screen.clear()
        screen.gotoXY(coluna, linha)
        print("*")
        time.sleep(5)

print("Você matou %s de %s monstros." % (acertos, tentativas))
