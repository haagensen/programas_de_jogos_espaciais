"""
As Minas de Astron
versão em Python por Christian Haagensen Gontijo, 30/06/2017
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

ano = 1                                      # ano
satisfacao = 1.0                             # fator de satisfação
minerio_armazenado = 0                       # quantidade de minério armazenado
numero_minas = random.randint(5, 8)          # número de minas
qtd_minerio = random.randint(80, 120)        # quantidade de minério produzido por mina
populacao = random.randint(40, 100)          # número de pessoas
grana = random.randint(10, 60) * populacao   # quantidade de dinheiro
preco_comida = random.randint(80, 120)       # preço da comida

while ano < 11:

    preco_minerio = random.randint(7, 19)    # preço de venda do minério
    preco_mina = random.randint(2000, 4000)  # preço de compra e venda de uma mina

    print("Ano %s\n" % ano)

    print("Existem %s habitantes na colônia." % populacao)
    print("Você dispõe de %s minas e $%s." % (numero_minas, grana))
    print("O fator de satisfação é %s\n" % satisfacao)

    print("Suas minas produziram %s toneladas cada uma." % qtd_minerio)
    minerio_armazenado += qtd_minerio * numero_minas
    print("Minério em estoque: %s toneladas." % minerio_armazenado)

    print("VENDAS")
    print("Preço de venda do minério: $%s por tonelada." % preco_minerio)
    print("Preço de venda das minas:  $%s por mina." % preco_mina)

    while True:
        minerio_vendido = to_int(input("Quantas toneladas de minério vai vender? "))
        if 0 <= minerio_vendido <= minerio_armazenado:
            break
    minerio_armazenado -= minerio_vendido
    grana += minerio_vendido * preco_minerio

    while True:
        minas_vendidas = to_int(input("Quantas minas vai vender? "))
        if 0 <= minas_vendidas <= numero_minas:
            break
    numero_minas -= minas_vendidas
    grana += minas_vendidas * preco_mina
    print("\nAgora você tem $%s\n" % grana)

    print("COMPRAS")
    while True:
        comida_comprada = to_int(input("Quanto quer gastar em comida? (aprox. $100/hab)"))
        if 0 <= comida_comprada <= grana:
            break
    grana -= comida_comprada

    if comida_comprada / populacao > 120:
        satisfacao += .1
    elif comida_comprada / populacao < 80:
        satisfacao -= .2

    while True:
        minas_compradas = to_int(input("Quantas minas quer comprar? "))
        if minas_compradas < 0 or minas_compradas * preco_mina > grana:
            pass
        else:
            break
    numero_minas += minas_compradas
    grana -= minas_compradas * preco_mina

    if satisfacao < 0.6:
        print("Os colonos se revoltaram")
        sys.exit(0)
    elif satisfacao < 0.9:
        qtd_minerio -= random.randint(1, 21)
    elif satisfacao > 1.1:
        qtd_minerio += random.randint(1, 21)

    if populacao / numero_minas < 10:
        print("Excesso de trabalho")
        sys.exit(0)

    if satisfacao > 1.1:
        populacao += random.randint(1, 11)
    elif satisfacao < 0.9:
        populacao -= random.randint(1, 11)

    if populacao < 30:
        print("População insuficiente")
        sys.exit(0)

    if random.randint(0, 1) < 0.1:
        print("Vazamento radioativo... muitos mortos")  # trágico, muito trágico...
        populacao //= 2

    if qtd_minerio > 150:
        print("Excesso de produção... queda dos preços")
        preco_minerio //= 2

    ano += 1

print("Você chegou ao fim do mandato")
