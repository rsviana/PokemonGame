import pickle
from pokemon import *
from pessoa import *

def escolherPokemonInicial(player):
    print("Olá {}, voce pode escolher agora o Pokemon que irá lhe acompanhar nessa jornada".format(player))
    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    acquaPoke = PokemonAgua("AcquaPoke", level=1)

    print("Voce possui 3 escolhas: ")
    print("1  -", pikachu)
    print("2  -", charmander)
    print("3  -", acquaPoke)

    while True:
        opcao = input("Escolha seu Pokemon: ")
        if opcao == "1":
            player.captura(pikachu)
            break
        elif opcao == "2":
            player.captura(charmander)
            break
        elif opcao == "3":
            player.captura(acquaPoke)
            break
        else:
            print("Escolha invalida")

def salvarGame(player):
    try:
        with open("database.db","wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo Salvo")
    except Exception as error:
        print("Erro ao salvar")
        print(error)

def carregarGame():
    try:
        with open("database.db","rb") as arquivo:
            player = pickle.load(arquivo)
            print("|         Jogo Carregado com sucesso!!          |")
            return player
    except Exception as error:
        print("Erro ao carregar o game! Jogo nao salvo")


if __name__ == "__main__":
    print("+-----------------------------------------------+")
    print("| Bem-vindo ao Game Pokemon RPG - For Terminal  |")
    print("+-----------------------------------------------+")
    player = carregarGame()
    if not player:
        print()
        nome = input("Olá, qual o seu nome: ")
        print()
        player = Player(nome)
        print("Oi {}, esse é um mundo habitado por Pokemons, a partir de agora você deve se tornar um mestre Pokemon".format(player))
        print("Capture o maximo de Pokemons que conseguir e lute com seus inimigos,")
        print()
        print("Seu saldo inicial $ {}".format(player.mostrarDinheiro()))
        if player.pokemons:
            print()
            print("Pelo visto voce já tem alguns Pokemons")
            print()
            player.mostraPokemomn()
        else:
            print("Voce ainda não tem Pokemons.")
            escolherPokemonInicial(player)

        print("Agora que voce ja tem um Pokemon, voce pode enfrentar seu oponente")
        inimigo = Inimigo("Bernardo",pokemon=[PokemonAgua("Amiguinho d'agua", level=1)])
        player.batalhar(inimigo)
        salvarGame(player)
    while True:
        print("+-----------------------------------------------+")
        print("O que voce deseja fazer?")
        print("1 - Explorar o mapa")
        print("2 - Lutar com inimigo")
        print("3 - Ver Pokeagenda")
        print("0 - Sair do Jogo")
        escolha = input("Escolha a opção desejada: ")

        if escolha == "0":
            break
        elif escolha == "1":
            player.explorar()
            salvarGame(player)
        elif escolha == "2":
            inimigoAleatorio = Inimigo()
            player.batalhar(inimigoAleatorio)
            salvarGame(player)
        elif escolha == "3":
            player.mostraPokemomn()
        else:
            print("Escolha invalida")
