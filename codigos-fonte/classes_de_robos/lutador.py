from .robo import Robo
from random import uniform

class RoboLutador(Robo):
    dano_maximo = 0.9
    dano_minimo = 0.4

    def __init__(self, nome:str) -> None:
        super().__init__(nome)
        self.poder = uniform(RoboLutador.dano_minimo, RoboLutador.dano_maximo)

    def __repr__(self):
        return f"RoboLutador(nome='{self.nome}', vida={self.vida:.2f}, poder={self.poder:.2f})"

    @property
    def poder(self) -> float:
        return self.__poder
    
    @poder.setter
    def poder(self, valor:float) -> None:
        if(valor < 0 or valor > RoboLutador.dano_maximo):
            raise ValueError(f"O poder de luta do robo deve ser entre 0 e {RoboLutador.dano_maximo}")
        
        self.__poder = valor

    def atacar(self, alvo:Robo) -> None:
        print(f"{self.nome} ataca {alvo.nome}!")
        alvo.vida *= (1 - self.poder)

        if(isinstance(alvo, RoboLutador)):
            print(f"{alvo.nome} contra-ataca {self.nome}\n")
            self.vida *= (1 - alvo.poder)