from pokemonEau import pokemonEau
class pokemonCroisiere(pokemonEau)
    def __init__(self, nom: str, poids: float, nbNageoires: int):
        self.__nom = nom
        self.__poids = poids
        self.__nbNageoires = nbNageoires