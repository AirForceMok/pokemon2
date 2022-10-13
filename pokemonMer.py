from pokemonEau import pokemonEau
class pokemonMer(pokemonEau)

    def __init__(self, nom: str, poids: float , nbNageoires, vitesse : float):
        self.__nom = nom
        self.__vitesse = vitesse

     return f"Je suis le pokémon {self.__nom} mon poids est de {self.__poids} "ma vitesse est de {self.__vitesse}" \
               f "je possède {self.__nbNageoires} nageoires" \

    @poids.setter
    def poids(self, poids: int):
        if poids > 0:
            self.__poids = poids

    @nbNageoires.setter
    def nbNageoires(self, nbNageoires: int):
        if nbNageoires > 0:
            self.__nbNageoires = nbNageoires
