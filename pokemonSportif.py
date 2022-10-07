from pokemonTerre import pokemonTerre
class pokemonSportif(pokemonTerre)
    def __init__(self, nom: str, poids: float , nbPattes : int, taille : float, frequence_cardiaque : int):
        self.__nom = nom
        self.__poids = poids
        self.__nbPattes = nbPattes
        self.__taille = taille
        self.__frequence_cardiaque = frequence_cardiaque
