"""
Salvamento no Espaço (Space Rescue)
versão em Python por Christian Haagensen Gontijo, 28/02/2019.

Você precisa fazer uma viagem urgente a um planeta distante, do outro lado da
Galáxia, para entregar remédios. A viagem é tão longa que você tem que fazê-la
em estado de hibernação. Antes de partir, o computador lhe pergunta quanta 
energia vai destinar aos motores, ao sistema de controle ambiental e à blindagem
da nave.

Quando você acorda, o computador lhe informa sobre o que aconteceu durante a
viagem; se tudo correu bem, você está em órbita em torno do planeta. Agora
precisa distribuir a energia que resta entre os retrofoguetes e a blindagem
térmica, de modo a fazer uma boa aterrissagem.

Se conseguir cumprir a missão, será promovido a Almirante do Espaço. Boa sorte!
"""
import random
import math
import sys
import time


def input_abs_int(mensagem):
    """ Pede um valor, e o retorna como um inteiro positivo, ou zero se não
    conseguir realizar a conversão.
    """
    valor = input(mensagem + " ")
    v = 0
    try:
        v = abs(int(valor))
    except:
        pass
    return v


print("Salvamento no Espaço\n")

instrucoes = input("Você precisa de instruções? ")
if instrucoes.upper()[0] == "S":
    print("\nVocê vai embarcar em uma missão para levar suprimentos médicos"
          "\npara um planeta distante.")
    print("Primeiro você precisa preparar a nave para a viagem, distribuindo a "
          "\nenergia disponível entre os motores, a blindagem e o controle "
          "\nambiental. Você então viaja em estado de hibernação, e quando "
          "\nacorda recebe um relatório sobre o que aconteceu no caminho.")
    print("Agora você precisa pousar no planeta...")
    i = input("Aperte qualquer tecla ")

distancia = random.randint(101, 800)  # int(rnd*800+101)
energia = random.randint(400, 801)    # int(rnd*400+401)
tempo = int(distancia / math.sqrt(energia / 5) + .5)

print("O planeta está a %s unidades de distância." % distancia)
print("Você tem %s unidades de energia, e deve chegar em %s dias.\n"
      % (energia, tempo))

while True:
    energia_motores = input_abs_int("Distribuição de energia para os motores?")
    energia_ambiental = input_abs_int("Para o controle ambiental?")
    energia_blindagem = input_abs_int("Para a blindagem?")
    if energia_motores + energia_ambiental + energia_blindagem <= energia:
        break

energia_disponivel = energia - energia_motores - energia_ambiental - energia_blindagem
velocidade = int(math.sqrt(energia_motores))
# Essa verificação aqui NÃO existia na versão BASIC original...
if velocidade == 0:
    tempo_dormindo = int(distancia)
else:
    tempo_dormindo = int(distancia / velocidade)

print("Sua velocidade é ", velocidade)
print("Você dormiu %s dias\n" % tempo_dormindo)

# O trecho abaixo é interessante (na versão BASIC) por mostrar um loop FOR
# onde há vários "GOTO 430" que saltavam para a próxima iteração do loop;
# ou seja, simulava com uma função "continue" (que o BASIC não tinha).
for i in range(1, random.randint(6, 11)):

    if random.randint(0, 1) > .5:
        continue

    # Outro trecho interessante no BASIC: um GOTO que vai para
    # determinada linha, dependendo de um número aleatório:
    #    310 GOTO 320 + INT(RND*4)*30
    # ou, em alguns computadores:
    #    310 ON INT(RND*4+1) GOTO 320, 350, 380, 410
    # minha versão em Python é um tanto mais simples.
    rnd = random.randint(1, 4)
    if rnd == 1:
        print("Chuva de asteróides... blindagem danificada")
        energia_blindagem = energia_blindagem - 20 - random.randint(1, 40)
    elif rnd == 2:
        print("Defeito no computador... parada para reparos")
        distancia = distancia + random.randint(1, 20)
    elif rnd == 3:
        print("Defeito no motor... velocidade reduzida")
        velocidade = velocidade - .5
    else:
        print("Radiação cósmica... defeito no controle ambiental")
        energia_ambiental = energia_ambiental - 20 - random.randint(1, 40)

    # Na falta de uma instrução "sleep", o BASIC tinha aqui (linhas 430-440)
    # um laço FOR vazio...
    time.sleep(.5)

# Essa verificação aqui NÃO existia na versão BASIC original...
if velocidade == 0:
    tempo_dormindo = int(distancia)
else:
    tempo_dormindo = int(distancia / velocidade)

print("Chegou em %s dias" % tempo_dormindo)
if energia_blindagem < 0:
    print("Blindagem destruída. Sua nave explodiu")
if energia_ambiental <= 0:
    print("Controle ambiental inoperante. Você morreu")
if velocidade <= 0:
    print("Motores inoperantes")
if tempo_dormindo > tempo:
    print("Você levou tempo demais")
if (energia_blindagem < 0) or (energia_ambiental <= 0) or \
   (velocidade <= 0) or (tempo_dormindo > tempo):
    sys.exit()

gravidade = random.randint(5, 10)
Gravidade = "alta"
if gravidade < 12:
    Gravidade = "média"
elif gravidade < 8:
    Gravidade = "baixa"

atmosfera = random.randint(5, 10)
Atmosfera = "densa"
if atmosfera < 12:
    Atmosfera = "média"
elif atmosfera < 8:
    Atmosfera = "rarefeita"

print("\nVocê agora está em órbita")
print("Energia disponível:", energia_disponivel)
print("A gravidade é", Gravidade)
print("A atmosfera é", Atmosfera, "\n")

while True:
    energia_retrofoguetes = input_abs_int("Energia para os retrofoguetes?")
    energia_blindagem = input_abs_int("Energia para a blindagem térmica?")
    if (energia_retrofoguetes + energia_blindagem) <= energia_disponivel:
        break

if energia_retrofoguetes < (gravidade * 10):
    print("Você fez uma cratera nova")
    sys.exit()

if energia_blindagem < (atmosfera * 10):
    print("Você é uma linda estrela cadente")
    sys.exit()

print("Você pousou lindamente... parabéns")
if (energia_disponivel - energia_blindagem - energia_retrofoguetes) > 25:
    sys.exit()
print("Pena que você não tem energia suficiente para abrir a escotilha")  # caramba!
