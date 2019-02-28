"""
Viagem ao Futuro (Trip into the Future)
Versão em Python por Christian Haagensen Gontijo, 25/07/2017.

Imagine que você está em uma espaçonave viajando com uma velocidade próxima da
luz. O tempo passa mais lentamente na espaçonave do que na Terra. Assim, depois
de uma longa viagem, você pode voltar à Terra em uma data posterior à indicada
pelo relógio da nave.

Neste jogo, o computador diz quantos anos deverão ter passado na Terra até a sua
volta. Você então tem que escolher a distância a ser percorrida (em anos-luz) e
a velocidade da nave (em relação à velocidade da luz) para chegar à Terra na
data prevista. Cuidado para não viajar para muito longe e muito devagar, ou
poderá morrer de velhice no caminho.
"""
import random
import math


def to_int(valor):
    v = 0
    try:
        v = int(valor)
    except:
        pass
    return v

print("Viagem ao Futuro")

tempo = random.randint(25, 125)
print("Você deve voltar daqui a %s anos.\n" % tempo)

# Temos aqui, no código BASIC original, a seguinte construção para
# obtenção da velocidade da nave:
#
# 70 PRINT "VELOCIDADE DA NAVE (0-1)"
# 80 INPUT V
# 90 IF V>=1 OR V<=0 THEN GOTO 70
#
# Por si só, seria curioso uma nave ter somente uma velocidade 0 ou 1.
# Mas o IF na linha 90 tem um evidente bug: qualquer número que você informar
# SEMPRE fará com que o código volte à linha 70, incluindo aí os "valores
# válidos" zero e um.
#
# Há outro problema, pouco à frente, na linha 120:
#
# 120 LET T1=D/V
#
# Supondo que o bug anterior tenha sido corrigido e a velocidade for zero,
# o programa pára com a exceção "ZeroDivisionError".
#
# Posto isto, vou pedir desculpas aos puristas e me permitir "alterar
# o clássico".
#
while True:
    velocidade = to_int(input("Velocidade da nave (1-10)? "))
    if 1 <= velocidade <= 10:
        break

distancia = to_int(input("Distância a percorrer? "))

t1 = distancia / (velocidade+1)

# A seguir, outro possível bug do código original, ainda envolvendo a "nave com
# velocidade 0 ou 1":
#
# 130 LET T2=T1/SQR(1-V*V)
#
# SQR é a função do BASIC que calcula uma raiz quadrada.
#
# Se V for 1, como prega o original, temos que SQR(1-V*V) = SQR(1-1) = 0,
# portanto o divisor zero levaria a *outra* exceção "ZeroDivisionError".
#
# O problema não acaba aí. Sendo, na versão Python, a velocidade da nave entre
# 1 e 10, esta linha iria gerar, para cada valor de V maior que 1, uma raiz
# quadrada de um número negativo -- ou seja, um número imaginário.
#
# Em resumo: se V=1, temos uma divisão por zero. Se V>1, temos um número
# imaginário. Acho que não era bem isso que os autores tinham em mente,
# quanto criaram este programa...
#
# Correção aplicada? Rápida e suja: tirei o "1-" da jogada...
#
t2 = t1 / math.sqrt(velocidade ** 2)

print("Você levou %2.2f anos e chegou depois de %2.2f anos." % (t1, t2))
if t1 > 50:
    print("Você morreu no caminho")
elif abs(tempo - t2) <= 5:
    print("Você chegou na hora")
elif (tempo-t2) > 5:
    print("Você chegou muito cedo")
elif (tempo - t2) < -5:
    print("Você chegou muito tarde")
