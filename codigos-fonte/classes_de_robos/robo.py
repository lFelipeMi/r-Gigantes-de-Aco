class Robo():
    Robo.nivel_critico = 0.40
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.vida = random.random()

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        if "-" in nome:
            if len(nome) > 11 or len(nome) < 2:
                raise ValueError("Nome com '-' deve ter entre 2 e 11 caracteres.")
        else:
            if len(nome) > 5 or len(nome) < 2:
                raise ValueError("Nome sem '-' deve ter entre 2 e 5 caracteres.")
        
        self.__nome = nome

    @property
    def vida(self) -> float:
        return self.__vida

    @vida.setter
    def vida(self, valor:float) -> None:
        if(valor < 0 and valor > 1):
            raise ValueError("Atributo deve ser maior que 0 e menor que 1")
        
        self.__vida = vida
    
    def precisa_de_medico() -> bool:
        return self.vida < Robo.nivel_critico

    def __add__(self, outroRobo: "Robo") -> "Robo":
        nome_pai = self.nome.split("-")[0]
        nome_mae = outroRobo.nome.split("-")[0]
        
        nome_bebe = nome_pai + '-' + nome_mae
        
        return Robo(nome_bebe)
        