# Personagem: Classe mae
# Heroi: controlado pelo usuário derivado da classe mae
# Inimigo: adversário dp usuario derivado da classe mae

from random import randint

class personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
        
    def get_vida(self):
        return self.__vida
        
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \n Vida: {self.get_vida()} \n Nivel: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
  
    def atacar(self, alvo):
        dano = randint(self.get_nivel() * 1, self.get_nivel() * 3)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
            
class Heroi(personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \n Habilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo):
        dano = randint(self.get_nivel() * 4, self.get_nivel() * 6)
        alvo.receber_ataque(dano)
        return print(f"{self.get_nome()} atacou com sua {self.get_habilidade()} o {alvo.get_nome()} e causou {dano} de dano!")
    
class Inimigo(personagem):
    def __init__(self, nome, vida, nivel, habilidade, tipo):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        self.__tipo = tipo

    def get_habilidade(self):
        return self.__habilidade
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \n Habilidade: {self.get_habilidade()} \n Tipo: {self.get_tipo()}"

    def ataque_especial(self, alvo):
        dano = randint(self.get_nivel() * 4, self.get_nivel() * 6)
        alvo.receber_ataque(dano)
        return print(f"{self.get_nome()} atacou com sua habilidade 1de {self.get_habilidade()} o {alvo.get_nome()} e causou {dano} de dano!")

    def ataque__super_especial(self, alvo):
        dano = randint(self.get_nivel() * 7, self.get_nivel() * 10)
        alvo.receber_ataque(dano)
        print ("ATAQUE SUPER !!!!!!")
        return print (f" O {self.get_nome()} Misturou seu tipo {self.get_tipo()} com sua habilidade de {self.get_habilidade()} e atacou o {alvo.get_nome()} e causou {dano} de dano.")

class jogo():
    """
    Classe orquestradora do jogo
    """
    def __init__(self, heroi, inimigo) -> None:
            self.heroi = heroi
            self.inimigo = inimigo

    def Iniciar_Batalha(self):
        """
        Fazer a gestão da batlha
        """
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("Personagens: \n")
            print(self.heroi.exibir_detalhes())

            print(self.inimigo.exibir_detalhes())

            escolha = int(input("Escolha: \n 1. Ataque Normal \n 2. Ataque Especial \n " " "))

            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)

            inimigo_ataque = randint(1, 3)
            
            if inimigo.get_vida() > 0:
                if inimigo_ataque == 1:
                    self.inimigo.atacar(self.heroi)
                elif inimigo_ataque == 2:
                    self.inimigo.ataque_especial(self.heroi)
                elif inimigo_ataque == 3:
                    self.inimigo.ataque__super_especial(self.heroi)

            if self.heroi.get_vida() > 0:
                print("Parabéns você ganhou o game")
            else:
                print("Você foi derrotado")

heroi = Heroi(nome = "Heroi", vida = 300, nivel = 5, habilidade = "Super Forca")
inimigo = Inimigo(nome="Morcego", vida = 300, nivel = 3, habilidade = "Vento", tipo = "Voador")
jogo = jogo(heroi, inimigo)
jogo.Iniciar_Batalha()
