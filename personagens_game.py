import random

class ser:
    def __init__(self, nome, level, vida):
        self.nome = nome
        self.level = level
        self.vida = vida

class Humano(ser):

    def __init__(self, nome):
        super().__init__(nome, level=1, vida=50)
        self.xp = 0

    def xp_para_proximo_level(self):
        return 100 * self.level

    def ganhar_xp(self, ganho):
        self.xp += ganho

        while self.xp >= self.xp_para_proximo_level():
            self.xp -= self.xp_para_proximo_level()
            self.level += 1
            print("Level Up!")
            print(f"XP: {self.xp}")
            
class monstro(ser):
    pass

class fight:
    print("Começando a luta")

class Jogo:
  """ Classe orquestradora do jogo """

  def __init__(self) -> None:
    self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
    self.inimigo = Inimigo(nome="Morcego", vida=80, nivel=5, tipo="Voador")

  def iniciar_batalha(self):
    """ Fazer a gestão da batalha em turnos """
    print("Iniciando batalha!")
    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhes dos Personagens:")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input("Pressione Enter para atacar...")
      escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

      if escolha == '1':
        self.heroi.atacar(self.inimigo)
      elif escolha == '2':
        self.heroi.ataque_especial(self.inimigo)
      else:
        print("Escolha inválida. Escolha novamente.")

      if self.heroi.get_vida() > 0:
        # Inimigo ataca o heroi
        self.inimigo.atacar(self.heroi)

    if self.heroi.get_vida() > 0:
      print("\nParabéns você venceu a batalha!")
    else:
      print("\nVocê foi derrotado!")

input_humano = humano(nome=input("Digite o nome do humano: "))

print(f"O nome do humano é: {input_humano.nome}")
print(f"O level do humano é: {input_humano.level}")
print(f"A vida do humano é: {input_humano.vida}")

#xp = 0
#if xp < 100:
#    
#    print(f"XP atual: {xp}")

aranha = monstro(nome="Aranha", level=2, vida=30)

rat = monstro(nome="Rat", level=1, vida=10)

rock = monstro(nome="Rock", level=1, vida=100)

bruiser = monstro(nome="Bruiser", level=5, vida=80)

goblin = monstro(nome="Goblin", level=3, vida=35)

slime = monstro(nome="Slime", level=1, vida=20)

skull = monstro(nome="Skull", level=4, vida=50)

goblin_group = monstro(nome="Goblin Group", level=5, vida=70)

big_slime = monstro(nome="Big Slime", level=3, vida=50)

poison_flower = monstro(nome="Poison Flower", level=7, vida=150)

Dragao = monstro(nome="Dragão", level=10, vida=300)

kungfu_panda = monstro(nome="Kung Fu Panda", level=80, vida=2000)

mickey_mouse = monstro(nome="Mickey Mouse", level=65, vida=1500)

incridible_hulk = monstro(nome="Incrível Hulk", level=900, vida=25000)

monstros = [aranha, goblin, slime, skull, goblin_group, big_slime, poison_flower, Dragao, kungfu_panda, mickey_mouse, incridible_hulk]
while True:
    monstro_batalha = random.choice(monstros)
    print(f"\nUm {monstro_batalha.nome} apareceu!")
    print(f"Level: {monstro_batalha.level} | Vida: {monstro_batalha.vida}")

    lutar = input("Deseja lutar contra o monstro? (s/n): ")

    if lutar == "s":
        print(f"Você decidiu lutar contra o {monstro_batalha.nome}!")
        break

    elif lutar == "n":
        if monstro_batalha.level > input_humano.level + 5:
            print("O monstro é muito forte. Você morreu!")
            break
        else:
            sorteio = random.randint(1, 10)
            if sorteio <= 7:
                print("Você conseguiu fugir!")
                continue  # 🔁 reinicia o jogo com novo monstro
            else:
                print("Você tentou fugir, mas o monstro te pegou!")
                print("Você é forçado a lutar!")
                break

    else:
        print("Opção inválida. Digite 's' ou 'n'.")

print("Fim do jogo.")


