from pokemonTerre import pokemonTerre
class pokemonCasanier(pokemonTerre)
    def __init__(self, nom: str, poids: float, taille: float, nbPattes: int, vitesse: float, nbHeures : float):
        self.__vitesse = vitesse
        self.__nbHeures = nbHeures

return f"Je suis le pokémon {self.__nom} mon poids est de {self.__poids} ma vitesse est de {self.__vitesse}" \
               f" je possède {self.__nbPattes} pattes, ma taille est de {self.__taille}" \

    def vitesse(self) -> float:
        pass


    @property
    def nom(self):
    return self.__nom

    @property
    def poids(self):
    return self.__poids
