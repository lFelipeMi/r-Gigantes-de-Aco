from .robo import Robo
from random import random

class RoboMedico(Robo):
    def __init__(self, nome:str) -> None:
        super().__init__(nome)
        self.poder_de_cura = random()

    def __repr__(self):
        return f"RoboMedico(nome='{self.nome}', vida={self.vida:.2f}, poder de cura={self.poder_de_cura:.2f})"

    @property
    def poder_de_cura(self) -> float:
        return self.__poder_de_cura

    @poder_de_cura.setter
    def poder_de_cura(self, valor:float) -> None:
        if(valor < 0 or valor > 1):
            raise ValueError("O poder de cura do robo não deve estar entre 0 e 1")

        self.__poder_de_cura = valor

    def curar(self, alvo:Robo) -> None:
        if(alvo.vida >= 1):
            raise ValueError(f"O robo {alvo.nome} não precisa de cura. Vida cheia!")

        if(alvo.vida > self.vida):
            print(f"O médico {self.nome} é incapaz de curar {alvo.nome} pois sua vida é insuficiente!")
        else:
            alvo.vida = min(1, alvo.vida + self.poder_de_cura)
            print(f"Vida de {alvo.nome} em {alvo.vida:.2f}")

