from pokemon import pokemon
class pokemonEau(pokemon)
    def __int__(self, nom: str, poids: float , nbNageoires):
    self.__nbNageoires = nbNageoires

    def vitesse(self) -> float:
        pass

    @property
    def nom(self):
        return self.__nom

    @property
    def poids(self):
        return self.__poids
