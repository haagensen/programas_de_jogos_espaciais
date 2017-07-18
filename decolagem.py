"""
Decolagem
versão em Python por Christian Haagensen Gontijo, 16/07/2017
"""

import random
import sys


def to_int(valor):
    v = 0
    try:
        v = int(valor)
    except:
        pass
    return v


print("Decolagem")

gravidade = random.randint(1, 20)
peso = random.randint(1, 40)
r = gravidade * peso

print("Gravidade ", gravidade)
for tentativa in range(11):
    palpite = to_int(input("Diga angulo força: "))

    if palpite > r:
        print("Muito grande", end="")
    elif palpite < r:
        print("Muito pequena", end="")
    else:
        print("Boa viagem")
        sys.exit()

    if tentativa != 10:
        print(", tente de novo")

print("")
print("Você falhou")
print("e foi capturado")
