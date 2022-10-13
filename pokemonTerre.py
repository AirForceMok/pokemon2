from pokemon import pokemon

class pokemonTerre(pokemon)
    def __init__(self, nom: str, poids: float , taille : float, nb_Pattes : int, vitesse : float):
        self.__nbPattes = nbPattes
        self.__taille = taille

    def __str__(self):
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
