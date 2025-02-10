from .robo import Robo

class RoboMedico(Robo):
    def __init__(self, nome:str) -> None:
        super().__init__(nome)
        self.poder_de_cura = random.random()

    @property
    def poder_de_cura(self) -> float:
        return self.__poder_de_cura

    @poder_de_cura.setter
    def poder_de_cura(self, valor:float) -> None:
        if(valor < 0 or valor > 1):
            raise ValueError("O poder de cura do robo não deve estar entre 0 e 1")

        self.__poder_de_cura = valor

    def curar(self, alvo:'Robo') -> None:
        if(alvo.vida >= 1):
            raise ValueError(f"O robo {alvo.nome} não precisa de cura. Vida cheia!")

        if(alvo.vida > self.vida):
            raise ValueError(f"O médico {self.nome} é incapaz de curar {alvo.nome} pois sua vida é insuficiente!")

        alvo.vida = min(1, alvo.vida + self.poder_de_cura)

    def __add__(self, outro:"Robo") -> "Robo":
        nome_pai = self.nome.split("-")[0]
        nome_mae = outroRobo.nome.split("-")[0]
        
        nome_bebe = nome_pai + '-' + nome_mae
        
        return RoboMedico(nome_bebe)
