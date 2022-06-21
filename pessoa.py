import random
from pokemon import *

NOME = ["Zakeu","Barney","Dennis","Zabbika"]
POKEMONS = [
    PokemonFogo("FirePoker"),
    PokemonFogo("Charmander"),
    PokemonFogo("MasterFire"),
    PokemonAgua("WatherPoker"),
    PokemonAgua("PokerAguar"),
    PokemonAgua("Molhadinho"),
    PokemonEletrico("Pikachu")
]
class Pessoa:

    def __init__(self, nome=None, pokemons=[],dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOME)

        self.pokemons = pokemons

        self.dinheiro = dinheiro
    def __str__(self):
        return self.nome

    def mostraPokemomn(self):
        if self.pokemons:
            print("Pokemons de:",self)
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}" .format(index, pokemon))
        else:
            print("Voce ainda nao tem Pokemons")

    def escolherPokemon(self):
        if self.pokemons:
            pokemonEscolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemonEscolhido))
            return pokemonEscolhido
        else:
            print("Jogador sem Pokemons")


class Player(Pessoa):
    tipo = "Player"
    def captura(self,pokemon):
        self.pokemons.append(pokemon)
        print("{} capiturou um {}".format(self, pokemon ))

    def escolherPokemon(self):
        self.mostraPokemomn()
        if self.pokemons:
            while True:
                escolha = input("Escolha seu Pokemon: ")

                try:
                    escolha = int(escolha)
                    pokemonEscolhido = self.pokemons[escolha]
                    print("{} eu escolho voce".format(pokemonEscolhido))
                    return pokemonEscolhido
                except:
                    print("Escolha invalida")
        else:
            print("Jogador sem Pokemons")

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print("Um pokemon selvagem apareceu {}!".format(pokemon))

            escolha = input("Deseja capturar o Pokemon? (s/n)")
            if escolha == "s":
                if random.random() > 0.5:
                    self.captura(pokemon)
                else:
                    print("O {} fugiu".format(pokemon))
            else:
                print("Seguimos então.")
        else:
            print("Sua explocaração não deu em nada!")


    def mostrarDinheiro(self):
        print("Voce possui  $ {}".format(self.dinheiro))

    def ganharDinehiro(self,quantidade):
        self.dinheiro += quantidade
        print("Voce ganhou $ {}".format(quantidade))
        self.mostrarDinheiro()

    def batalhar(self, pessoa):
        print("{} inicitou uma batalha com {}".format(self,pessoa))

        pessoa.mostraPokemomn()
        pokemonInimigo = pessoa.escolherPokemon()

        pokemon = self.escolherPokemon()

        if pokemon and pokemonInimigo:
            while True:
                vitoria = pokemon.atacar(pokemonInimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganharDinehiro(pokemonInimigo.level * 100)
                    break
                vitoria_inimiga = pokemonInimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break

        else:
            print("Essa batalha nao pode acontecer")


class Inimigo(Pessoa):
    tipo = "Inimigo"
    def __init__(self,nome=None, pokemon=None):
        if not pokemon:
            pokemonsAleatorios = []
            for i in range(random.randint(1,6)):
                pokemonsAleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemonsAleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemon)





        

