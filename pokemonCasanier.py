from pokemonTerre import pokemonTerre
class pokemonCasanier(pokemonTerre)
    def __init__(self, nom: str, poids: float, nbPattes: int, taille: float, nbHeures: int):
        self.__nom = nom
        self.__poids = poids
        self.__nbPattes = nbPattes
        self.__taille = taille
        self.__nbHeures = nbHeures

