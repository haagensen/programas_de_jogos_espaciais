"""
Cinturão de Asteróides (Asteroid Belt)
Versão em Python por Christian Haagensen Gontijo, 30/04/2020.

Você está atravessando o Cinturão de Asteróides. Para não se chocar com eles, 
precisa destruí-los; a força necessária para isso depende do tamanho do 
asteróide.

Os asteróides aparecem na tela do seu computador como grupos de estrelas. Para 
destruí-los, você precisa apertar a tecla do número correspondente ao número de 
estrelas. Não perca tempo... os asteróides são muito velozes!
"""
import random
import time
from colorconsole import terminal  # obrigado, Nilo! <https://github.com/lskbr/colorconsole>


screen = terminal.get_terminal(conEmu=False)
# requisito no Linux e Mac-OS:
screen.enable_unbuffered_input_mode()

print("Cinturão de Asteróides\n" + "=" * 23)
time.sleep(2)
acertos = 0

for tentativas in range(10):  # dez chances!

    # Posição do "asteróide" na tela. Os computadores da época tinham algo
    # entre 16 (TRS-80) e 25 (Apple) linhas de resolução, e entre 32 (TK-82)
    # e 64 (TRS-80) colunas. A vida era bela! Hoje, temos terminais com larguras
    # variadas e muitas vezes rodando dentro de janelas numa interface gráfica,
    # o que torna as coisas um tanto mais complicadas. Irei, portanto, alterar
    # um pouco os valores...
    posicao_horizontal = random.randint(1, 35)  # original: 1~18
    posicao_vertical = random.randint(1, 20)    # original: 1~12

    # Tamanho do asteróide: entre 1 e 9.
    tamanho_asteroide = random.randint(1, 9)

    screen.clear()
    screen.gotoXY(0, posicao_vertical)
    for i in range(tamanho_asteroide):
        if i in (0, 3, 6):
            print("\n", " " * posicao_horizontal, end="")
        print("*", end="")  # sim, ISSO é parte do asteróide...
    print("")

    # Aqui, um código um tanto complicado de se traduzir do BASIC para o Python:
    #
    # 180 FOR I=1 TO 10
    # 190 LET Q=VAL("0"+INKEY$)
    # 200 IF Q<>0 THEN GOTO 240
    # 210 NEXT I
    #
    # O que este trecho faz é verificar se você está pressionando uma tecla no
    # teclado do seu computador -- não qualquer tecla, mas um número entre 1 e
    # 9 -- e salta para a "linha 240" se estiver.
    #
    # A função que faz esta leitura é "INKEY$". A função "VAL" converte o valor
    # lido em um número. "INKEY$" não pára o programa para esperar um pressio-
    # namento, daí ser normalmente usada dentro de um loop.
    #
    # Saímos do "loop" em duas condições: se a tecla pressionada for um número
    # diferente de zero, ou após 10 interações do loop.
    #
    # Isto foi evidentemente criado para dar um "tempo de resposta" máximo para
    # o jogador. Mas "quanto" tempo isso significa, é difícil de dizer... irá
    # variar muito de computador para computador; e, como estamos falando em
    # BASIC para computadores do início dos anos 80...
    #
    # Enfim. Na impossibilidade de executar exatamente como no original, tentei
    # emular o melhor possível esse bloco de código.

    inicio = time.perf_counter()
    while True:
        numero_pressionado = 0
        if screen.kbhit():
            tecla_pressionada = screen.getch()
            if b'1' <= tecla_pressionada <= b'9':
                numero_pressionado = int(str(tecla_pressionada)[2])
            break

        # Vamos dar ao jogador cerca de 3 segundos para escolher um número!
        if time.perf_counter() > inicio + 3:
            break

    if numero_pressionado == 0:
        print("Bateu no asteróide")
        time.sleep(2)
        continue

    if numero_pressionado < tamanho_asteroide:
        print("Muito fraco")
    elif numero_pressionado > tamanho_asteroide:
        print("Muito forte")
    else:
        print("Asteróide destruído")
        acertos += 1

    time.sleep(2)

print("Você acertou %s em 10" % acertos)
screen.restore_buffered_mode()
