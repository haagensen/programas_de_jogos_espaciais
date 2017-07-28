"""
Vale da Morte
Versão em Python por Christian Haagensen Gontijo, 27/07/2017

Só há um meio de escapar ao ataque dos perigosos Dissectitrons. Você vai ter que respirar 
fundo e entrar com a sua nave no perigoso desfiladeiro conhecido como Vale da Morte.

Seu computador vai querer saber a largura do vale. Comece com 15 e vá diminuindo aos poucos; 
8 já é bastante difícil. Dirija sua nave apertando Q para ir para a esquerda e P para ir 
para a direita, e veja se consegue atravessar o Vale da Morte.
"""
import random
import sys
import time
from colorconsole import terminal  # obrigado, Nilo! <https://github.com/lskbr/colorconsole>


def to_int(valor):
    v = 0
    try:
        v = int(valor)
    except:
        pass
    return v

screen = terminal.get_terminal(conEmu=False)
# requisito no Linux e Mac-OS:
screen.enable_unbuffered_input_mode()

print(" ---=======================--- ")
print(" ---==== Vale da Morte ====--- ")
print(" ---=======================--- ")
posicao = 0
posicao_final = 200

largura = to_int(input("Largura? "))
largura //= 2

parede_esquerda = 10
centro = largura
parede_direita = largura

#
#  |      parede_esquerda                     centro                         parede_direita
#  | <-----------------------> I <------------------------------> * <------------------------------> I
#  |  (10 espaços, no início)     ("largura" espaços, no início)     ("largura" espaços, no início)
#
#  ^
#  |
#  +-- borda da tela


while True:

    while True:
        diferenca = random.randint(-1, 1)
        if parede_esquerda + diferenca >= 0 or parede_esquerda + diferenca <= 20:
            break

    # Muda a posição das paredes, de acordo com o valor de "diferenca"
    parede_esquerda += diferenca
    centro -= diferenca
    parede_direita += diferenca

    #
    #  |
    #  | <-----------> I <-------------> * <-------------> I
    #  |  + diferença      - diferença       + diferença
    #
    #  ^
    #  |
    #  +-- borda da tela

    # No código BASIC original:
    # 150 SCROLL
    # Na falta de comando similar, vamos apenas colocar uma linha em branco...
    print("")

    coluna = parede_esquerda
    if coluna != 0:
        for i in range(coluna):
            print(" ", end="")
    print("I", end="")  # uma "parede"...
    coluna = centro
    if coluna != 0:
        for i in range(coluna):
            print(" ", end="")
    print("*", end="")  # a sua nave...
    coluna = parede_direita
    if coluna != 0:
        for i in range(coluna):
            print(" ", end="")
    print("I", end="")  # e a outra "parede"

    timeout = 0
    pressionado = ""
    while True:
        time.sleep(0.2)
        if screen.kbhit():
            pressionado = screen.getch().decode(sys.stdout.encoding).upper()
            break
        timeout += 1
        if timeout > 1:
            break

    if pressionado == 'Q':
        # nave vai para a esquerda
        centro -= 1
        parede_direita += 1
    elif pressionado == "P":
        # nave vai para a direita
        centro += 1
        parede_direita -= 1

    if centro < 1 or parede_direita < 1:
        print("\n\nVocê bateu e sua nave se desintegrou")
        screen.restore_buffered_mode()
        sys.exit()

    posicao += 1
    if posicao >= posicao_final:
        break

print("\n\nMuito bem... você conseguiu atravessar o Vale da Morte!")
screen.restore_buffered_mode()
