from abc import ABC, abstractmethod

class pokemon(ABCà)

    def __init__(self, nom: str, poids: float):
        self.__nom = nom
        self.__poids = poids

    def __str__(self): -> str:
        return f"Je suis le pokemon de {self.__nom}, mon poids est de {self.__poids}"

    abstractmethod()
    def vitesse(self) -> float:
        pass
    
    @property
    def nom(self):
            return self.__nom
    
    @property
    def poids(self):
            return self.__poids
