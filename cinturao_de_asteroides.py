"""
Cinturão de Asteróides
Versão em Python por Christian Haagensen Gontijo, 24/07/2017.

Você está atravessando o Cinturão de Asteróides. Para não se chocar com eles, precisa 
destruí-los; a força necessária para isso depende do tamanho do asteróide.

Os asteróides aparecem na tela do seu computador como grupos de estrelas. Para 
destruí-los, você precisa apertar a tecla do número correspondente ao número de 
estrelas. Não perca tempo... os asteróides são muito velozes!
"""
import random
import time
import sys
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

print("Cinturão de Asteróides")
acertos = 0
for g in range(10):
    posicao_horizontal = random.randint(1, 18)
    posicao_vertical = random.randint(1, 12)
    tamanho_asteroide = random.randint(1, 9)

    screen.clear()
    screen.gotoXY(0, 0)
    print("\n" * posicao_vertical)
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
    # Este trecho verifica se você está apertando uma tecla -- não qualquer tecla, mas uma com um
    # número entre 1 e 9 -- e pula para a "linha 240" se estiver.
    #
    # INKEY$ é a instrução que verifica o pressionamento da tecla, e retorna a tecla pressionada.
    # A instrução VAL, a seguir, transforma o valor retornado em um número, e só sai do "loop" se
    # o número for diferente de zero.
    #
    # Acontece que INKEY$ é do tipo "non blocking", ou seja, ela não pára o programa esperando
    # pelo pressionamento da tecla; daí ser geralmente usada dentro de um "loop" para
    # verificação do teclado.
    #
    # Outro problema é que o "for" é executado por um tempo I que é difícil de dizer, exatamente,
    # qual é -- ele não faz uma pausa de X segundos, mas usa um "tempo de processamento" que, sem
    # dúvida, variava muito de computador para computador; e, como estamos falando em BASIC para
    # computadores do início dos anos 80...
    #
    # Enfim. Na impossibilidade de executar exatamente como no original, tentei emular o melhor
    # possível esse bloco de código.

    timeout = 0
    numero_pressionado = 0
    while True:
        time.sleep(1)
        if screen.kbhit():
            numero_pressionado = to_int(screen.getch().decode(sys.stdout.encoding))
            if numero_pressionado > 0:
                print(numero_pressionado)
                break
        timeout += 1
        if timeout > 3:
            break

    if numero_pressionado == 0:
        print("Bateu no asteróide")
    else:
        # O "if" abaixo tem construção meio estranha, mas vou seguir o livro...
        if numero_pressionado != tamanho_asteroide:
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
