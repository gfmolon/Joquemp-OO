#jokempô OO
from random import randint

class Jogo():
    def __init__(self):
        self.__jogada = 0
        self.__jogada_pc = 0

    @property
    def jogada(self):
        return self.__jogada

    @property
    def jogada_pc(self):
        return self.__jogada_pc

    def apresentacao(self):
        print("***************************")
        print("         #jokempô OO")
        print("***************************")

    def pede_jogada(self):
        if self.__jogada == 0: #so pede jogada quando jogada = 0, ou seja quando chamo zera rodada.
            testa = int(input("Escolha sua Jogada:\n"
                         "(1)Pedra (2)Papel (3)Tesoura"))
            self.__jogada = testa
            if self.__jogada <= 0 or self.__jogada > 3: #testa 1 a 3
                self.__jogada = 0 #trava rodada
            print(f"Sua Jogada: {self.__jogada}")

            return self.__jogada

    def gera_jogada_pc(self):
        self.__jogada_pc = randint(1,3)
        print(f"Jogada PC: {self.__jogada_pc}")
        return self.__jogada_pc

    def zera_rodada(self):
        self.__jogada = 0
        self.__jogada_pc = 0

    def espacamento(self):
        print("***************************")


# 1 Pedra, # 2 Papel, # 3 Tesoura
    def resulta_a_rodada(self):
        if self.__jogada == self.__jogada_pc:
            print("Empate!")
        elif self.__jogada == 1 and self.__jogada_pc == 2:
            print("Você Perdeu! Papel ganha de Pedra!")
        elif self.__jogada == 2 and self.__jogada_pc == 1:
            print("Você Ganhou! Papel ganha de Pedra!")
        elif self.__jogada == 3 and self.__jogada_pc == 1:
            print("Você Perdeu! Pedra ganha de Tesoura!")
        elif self.__jogada == 1 and self.__jogada_pc == 3:
            print("Você Ganhou! Pedra ganha de Tesoura")
        elif self.__jogada == 3 and self.__jogada_pc == 2:
            print("Você Ganhou! Papel ganha de Pedra!")
        elif self.__jogada == 2 and self.__jogada_pc == 3:
            print("Você Perdeu! Papel ganha de Pedra!")

jogo = Jogo()
jogo.apresentacao()

x=0
for x in range(1,6): #5 rodadas
    jogo.pede_jogada()
    jogo.gera_jogada_pc()
    jogo.resulta_a_rodada()
    jogo.zera_rodada()
    jogo.espacamento()
    x =+1