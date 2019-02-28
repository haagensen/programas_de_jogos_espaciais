"""
Emboscada (Alien Snipers)
Versão em Python por Christian Haagensen Gontijo, 22/07/2017.
 
Você é o comandante de um cruzador interestelar que, por causa de um defeito nos
motores de hiperespaço, entrou em uma zona proibida. Sua nave está sendo atacada
por caças alienígenas, que, para tornar as coisas piores, estão usando um
aparelho de despistamento que faz com que o seu radar forneça leituras falsas.
Felizmente, o computador de bordo fornece um número de código que você pode usar
para calcular a posição correta das naves inimigas. Mas você precisa ser rápido,
elas não ficam muito tempo no mesmo lugar!
 
O computador imprime uma letra (a posição falsa do inimigo) e um número. Você
deve avançar no alfabeto esse número de letras e apertar a tecla correspondente.
Por exemplo, para M4 você deve apertar a tecla Q, para C2 a tecla E, e assim por
diante. Quando você aperta uma tecla, dispara automaticamente o canhão de laser,
e, se a letra estiver certa, destrói uma nave inimiga. Você pode escolher a
dificuldade de cada jogo, escolhendo um número de 1 a 10. Este número
corresponde ao maior número que pode aparecer no código. Em cada jogo, você é
atacado por 10 caças alienígenas. Veja quantos consegue acertar.
"""
import random
import sys
import time
from colorconsole import terminal  # obrigado, Nilo! <https://github.com/lskbr/colorconsole>

screen = terminal.get_terminal(conEmu=False)
# requisito no Linux e Mac-OS:
screen.enable_unbuffered_input_mode()


def to_int(valor):
    v = 0
    try:
        v = int(valor)
    except:
        pass
    return v

print("Emboscada")
print("")

while True:
    dificuldade = to_int(input("Dificuldade (1-10)? "))
    if 0 < dificuldade < 11:
        break

acertos = 0

for g in range(10):
    letra = chr(random.randint(65, 90 - dificuldade))
    numero = random.randint(1, dificuldade)
    print(letra, numero)

    # Aqui, um código um tanto complicado de se traduzir do BASIC para o Python:
    #
    # 140 FOR I=1 TO 20+D*5
    # 150 LET I$=INKEY$
    # 160 IF I$<>"" THEN GOTO 190
    # 170 NEXT I
    #
    # Este trecho verifica se você está apertando uma tecla, e pula para a "linha 190" se estiver.
    #
    # INKEY$ é a instrução que verifica o pressionamento da tecla, e retorna a tecla pressionada.
    # Acontece que ela é do tipo "non blocking", ou seja, ela não pára o programa esperando pelo
    # pressionamento da tecla; daí ser geralmente usada dentro de um "loop" para verificação do
    # teclado.
    #
    # Outro problema é que o "for" é executado por um tempo X que é difícil de dizer, exatamente,
    # qual é -- ele não faz uma pausa de X segundos, mas usa um "tempo de processamento" que, sem
    # dúvida, variava muito de computador para computador; e, como estamos falando em BASIC para
    # computadores do início dos anos 80...
    #
    # Enfim. Na impossibilidade de executar exatamente como no original, tentei emular o melhor
    # possível esse bloco de código.

    timeout = 0
    correspondente = ""
    while True:
        time.sleep(1)
        if screen.kbhit():
            correspondente = screen.getch().decode(sys.stdout.encoding).upper()
            print(correspondente)
            break
        timeout += 1
        if timeout > (13 - dificuldade):
            break

    if correspondente == chr(ord(letra) + numero):
        acertos += 1

print("Você acertou %s/10" % acertos)
screen.restore_buffered_mode()
