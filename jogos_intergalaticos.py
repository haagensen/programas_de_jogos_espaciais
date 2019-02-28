"""
Jogos Intergaláticos (Intergalactic Games)
versão em Python por Christian Haagensen Gontijo, 17/07/2017.

As redes de televisão da Terra estão competindo pela cobertura exclusiva dos
Primeiros Jogos Intergaláticos. A companhia que conseguir primeiro colocar um
satélite em órbita na altitude correta ganhará a concessão.

Você é o engenheiro que a Rede Século 21 encarregou de lançar o satélite. 
Será que vai conseguir lançá-lo com o ângulo e velocidade corretos?
"""
import random
import math
import sys


def to_int(valor):
    v = 0
    try:
        v = int(valor)
    except:
        pass
    return v

print("Jogos Intergaláticos")

altura = random.randint(1, 100)
print("Você deve lançar um satélite")
print("até uma altura de %s metros." % altura)

for tentativa in range(9):
    angulo = to_int(input("Diga o ângulo (0-90) "))
    velocidade = to_int(input("Diga a velocidade (0-40000) "))

    # usa 'altura' para calcular qual deve ser o ângulo, e subtrai do seu
    # palpite para ver se você chegou perto
    angulo -= math.atan(altura / 3) * 180 / math.pi

    # calcula a velocidade correta e subtrai do seu palpite
    velocidade -= 3000 * math.sqrt(altura + 1 / altura)

    if abs(angulo) < 2 and abs(velocidade) < 100:
        print("Você conseguiu")
        print("Ganhamos... graças a você")
        sys.exit()
    elif angulo < -2:
        print("Muito baixo")
    elif angulo > 2:
        print("Muito alto")

    if velocidade < -100:
        print("Muito lento")
    elif velocidade > 100:
        print("Muito rápido")

print("Você falhou")
print("Está despedido")
