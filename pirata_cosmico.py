

"""
Pirata Cósmico
versão em Python por Christian Haagensen Gontijo, 17/07/2017

Em algum lugar atrás de você, na escuridão do espaço, está a nave de Elron, o Pirata Cósmico.
Você sabe que ele está em algum ponto da rede tridimensional que aparece na tela da sua nave. 
Você dispõe de quatro bombas. Pode lançá-las, uma a uma, em posições espeificada por três
números entre 0 e 9, que deve fornecer ao computador da nave.
Conseguirá acertar a nave de Elron antes que o pirata o capture?
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

print("Pirata Cósmico")
tamanho_rede = 10
tentativas = 4

# a posição de Elron é fixada por essas três linhas
x = random.randint(1, tamanho_rede)
y = random.randint(1, tamanho_rede)
distancia = random.randint(1, tamanho_rede)

for i in range(tentativas + 1):
    x1 = to_int(input("Posição X (0 a 9)? "))
    y1 = to_int(input("Posição Y (0 a 9)? "))
    d1 = to_int(input("Distância (0 a 9)? "))

    if x == x1 and y == y1 and distancia == d1:
        print("")
        print("*BUUUM* você o pegou!!")
        sys.exit()

    print("Tiro foi para ", end="")
    if y1 > y:
        print("N", end="")
    elif y1 < y:
        print("S", end="")
    if x1 > x:
        print("E", end="")
    elif x1 < x:
        print("O", end="")
    print("")

    if d1 > distancia:
        print("Muito longe")
    elif d1 < distancia:
        print("Muito perto")

print("")
print("Você foi capturado!!")
