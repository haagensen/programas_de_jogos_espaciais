"""
Decolagem (Starship Takeoff)
versão em Python por Christian Haagensen Gontijo, 16/07/2017.

Você é o comandante de uma espaçonave. Sua nave caiu em um planeta desconhecido
e você precisa decolar rapidamente em uma nave alienígena que conseguiu
capturar. O computador da nave lhe diz qual é a força de gravidade do planeta,
mas você tem que adivinhar qual a força que deve imprimir aos motores para 
decolar. Se a força for muito pequena, a nave não conseguirá subir. Se for
muito grande, um mecanismo de segurança entrará em ação, desligando os motores
para evitar que fiquem superaquecidos. Se ainda estiver no planeta depois de 
dez tentativas, será capturado pelos alienígenas.
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

random.randint()
print("Decolagem")

gravidade = random.randint(1, 20)
peso = random.randint(1, 40)
r = gravidade * peso

print("Gravidade ", gravidade)
for tentativa in range(11):
    palpite = to_int(input("Diga a força: "))

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
