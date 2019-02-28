"""
Feras de Galacticon (Monsters of Galacticon)
versão em Python por Christian Haagensen Gontijo, 21/07/2017.

Pousar em Galacticon foi fácil... mas ninguém avisou a você que ali vivem
algumas das mais perigosas feras do Universo.

Ao ser atacado por um dos monstros, você precisa escolher uma de suas armas --
uma pistola de raios, um sabre de laser ou um triturador molecular -- para usar
contra ele. Se fizer a escolha correta, talvez consiga sobreviver para
conquistar Galacticon.
"""
import random
import sys

print("Feras de Galacticon")

monstros = ["Sulfacidor", "Flamgondar", "Balnolotin", "Golandor"]
numero_monstros = len(monstros)
astronautas = 5

for i in range(numero_monstros):
    a = random.randint(0, numero_monstros - 1)
    b = random.randint(0, numero_monstros - 1)
    monstros[a], monstros[b] = monstros[b], monstros[a]

for tentativa in range(7):

    # No código BASIC original:
    # 180 LET R=INT(RND*N+1)
    # onde "N" é a variável "numero_monstros"; a instrução retorna um número entre 1 e 4.
    # Como se verá a seguir, esta variável servirá para selecionar um dos "monstros";
    # portanto, no Python precisaremos de um valor entre 0 e 3...
    escolhido = random.randint(0, numero_monstros - 1)

    print("Monstro chegando...")
    print("É um", monstros[escolhido])
    while True:
        arma = input("Que arma? Pistola de [r]aio, [s]abre laser, ou [t]riturador molecular? ").upper()
        if arma in ("R", "S", "T"):
            break

    # Eis aqui um trecho complicado de traduzir do BASIC original para o Python:
    # 230 LET W=CODE(R$)-54+R
    # 240 LET W=W-3*(W>3)-3*(W>6)
    #
    # Com o seguinte texto, em uma caixa ao lado: "o computador usa os valores de R e R$
    # para calcular um número, W, que pode ser 1, 2 ou 3". Isto merece alguns comentários...

    # 230 LET W=CODE(R$)-54+R
    #
    # Primeiro ponto: a função "CODE". Segundo o manual do ZX-81, disponível em
    # <http://www.worldofspectrum.org/ZX81BasicProgramming/>, capítulo 11: "CODE is applied
    # to a string, and gives the code of the first character in the string (or 0 if the
    # string is empty)", e tais códigos estão entre 0 e 255 (sim, trata-se de uma tabela
    # proprietária -- esqueça Unicode, ou mesmo ASCII!). O "Apêndice A" do manual do ZX-81
    # nos diz que "R" vale 55, "S" vale 56 e "T" vale 57. Ora, temos que, em Python, o
    # ordinal de "R" é 82, então será preciso uma pequena adaptação ao código.
    #
    # Segundo ponto: a variável "R" (que, aqui, eu renomeei para "escolhido") é um número
    # que, no BASIC original, estará entre 1 e 4 (vide comentário acima) e que será usada
    # para selecionar um monstro da lista "monstros". No BASIC do ZX-81, um vetor tem "base
    # 1", ou seja, o monstro está entre 1 e 4. Já em Python (base 0), o monstro estará
    # entre 0 e 3.
    #
    # Assim sendo, no BASIC, o valor de "w" estará entre 2 e 7 (inclusive); no Python
    # estará entre 1 e 6 (inclusive).
    #
    w = ord(arma) - 81 + escolhido

    # 240 LET W=W-3*(W>3)-3*(W>6)
    #
    # Confesso nunca ter visto uma atribuição em BASIC que possua, em seus termos,
    # operadores de comparação -- mas vou assumir que as comparações funcionam como no
    # Python: "se verdadeiro, retorna 1; se falso, retorna zero". Lembrando do "vetor
    # base 1" do BASIC, é preciso um ajuste...
    #
    w = w - 3 * (w > 2) - 3 * (w > 5)

    # Enquanto "w" estará, em BASIC, entre 1 e 3, em Python estará entre 0 e 2.
    # Poderíamos deixar assim... mas vou adicionar 1 só para deixar igualzinho
    # à versão original.
    w += 1

    if w == 2:
        print("Você o matou")
        continue
    elif w == 3:
        print("Sem efeito")
        if random.randint(1) > 0.4:
            continue
        print("Você enfureceu o %s e ele matou um do seu grupo" % monstros[escolhido])
    else:
        print("Não adianta, comeu um do seu grupo")
    astronautas -= 1
    if astronautas < 1:
        print("Vocês morreram todos")
        sys.exit()

print("Você sobreviveu para conquistar Galacticon")
