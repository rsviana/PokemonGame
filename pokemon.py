import random


class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        self.level = level
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return "{}({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        ataqueEfetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataqueEfetivo
        print("{} perdeu {} de vida".format(pokemon, ataqueEfetivo))

        if pokemon.vida <= 0:
            print("{} perdeu a batalha".format(pokemon))
            return True
        else:
            return False

    def defesa(self,pokemon):
        print("{} defendeu {}".format(self.tipo, pokemon.tipo))

    def fugiu(self,pokemon):
        print("O Pokemon {} fugiu,  {} ganhou".format(self.tipo, pokemon.tipo, self.especie))


class PokemonEletrico(Pokemon):
    tipo = 'Elerico'
    def atacar(self, pokemon):
        print("{} atacou massivamente o {}".format(self, pokemon))
        return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = 'Fogo'
    def atacar(self, pokemon):
        print("{} atacou com FOGO o {}".format(self, pokemon))
        return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'Agua'
    def atacar(self, pokemon):
        print("{} atacou com jato de Agua o {}".format(self, pokemon))
        return super().atacar(pokemon)
