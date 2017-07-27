"""
Módulo Lunar
versão em Python por Christian Haagensen Gontijo, 20/07/2017

Você está no controle de um módulo lunar que está levando um
pequeno grupo de astronautas para a superfícia da Lua. Para
pousar com segurança, você precisa reduzir a velocidade disparando
um retrofoguete, mas seu suprimento de combustível é limitado.

O computador de bordo lhe diz qual é a altitude inicial, a velocidade
e o suprimento de combustível, e lhe pergunta a quantidade de combustível
que deseja queimar. Em seguida, calcula a nova altitude e velocidade.
Queimando cinco unidades de combustível, você mantém a velocidade constante.
Uma quantidade maior diminui a velocidade. Procure pousar com a menor
velocidade possível. Será que você vai conseguir pousar na Lua?
"""


def to_int(valor):
    v = 0
    try:
        v = int(valor)
    except:
        pass
    return v

print("Módulo Lunar")
tempo = 0
altitude = 500.0
velocidade = 50
combustivel = 120

while True:

    print("Tempo.....: %-5s    Altitude...: %s" % (tempo, altitude))
    print("Velocidade: %-5s    Combustível: %s" % (velocidade, combustivel))

    # Só queimamos combustível se ainda houver combustível...
    if combustivel != 0:
        queimar = to_int(input("Queima? (0-30) "))
        if queimar > 30:
            queimar = 30
    if queimar > combustivel:
        queimar = combustivel

    nova_velocidade = velocidade - queimar + 5
    combustivel -= queimar

    # Se a distância percorrida desde a última queima é superior à altitude, você pousou a nave
    if (nova_velocidade + velocidade) / 2 >= altitude:
        break

    altitude -= (nova_velocidade + velocidade) / 2
    tempo += 1
    velocidade = nova_velocidade

# Verificamos se este foi um pouso seguro
nova_velocidade = velocidade + (5 - queimar) * altitude / velocidade
print("")
if nova_velocidade > 5:
    print("Vocês caíram... todos mortos")
elif 1.0 < nova_velocidade <= 5:
    print("OK... mas alguns feridos")
elif nova_velocidade <= 1:
    print("Boa aterrisagem")
