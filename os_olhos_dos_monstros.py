"""
Os Olhos dos Monstros
versão em Python por Christian Haagensen Gontijo, 30/06/2017
"""

import time
import random
from colorconsole import terminal  # obrigado, Nilo! <https://github.com/lskbr/colorconsole>

screen = terminal.get_terminal(conEmu=False)


def cls():
    screen.clear()
    screen.gotoXY(0, 0)


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
    cls()
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
        cls()
        screen.gotoXY(coluna, linha)
        print("*")
        time.sleep(5)

print("Você matou %s de %s monstros." % (acertos, tentativas))
