from pokemonTerre import pokemonTerre
class pokemonSportif(pokemonTerre)
    def __init__(self, nom: str, poids: float , nbPattes : int, taille : float, frequence_cardiaque : int, vitesse : float):
        self.__vitesse = vitesse
        self.__frequence_cardiaque = frequence_cardiaque

    def __str__(self):
        return f"Je suis le pokémon {self.__nom} mon poids est de {self.__poids} ma vitesse est de {self.__vitesse}"\
               f" je possède {self.__nbPattes} pattes, ma taille est de {self.__taille}",\
               f" ma fréquence cardiaque est de {self.__frequence_cardiaque} pulsations à la minute"

    def vitesse(self) -> float:
        pass


    @property
    def nom(self):
    return self.__nom

    @property
    def poids(self):
    return self.__poids
