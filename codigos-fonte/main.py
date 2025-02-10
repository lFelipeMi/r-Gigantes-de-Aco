from classes_de_robos import Robo, RoboMedico, RoboLutador
from random import choice

def simular_luta(grupo, equipeM, tipo_simulacao:str):

    if(tipo_simulacao == 'Fases_de_Grupos'):
        print("\n--- Iniciando Lutas no Grupo ---")

    if(tipo_simulacao == 'Final'):
        print("\n--- Final do Campeonato ---")
    
    print('Lutadores:')
    for lutadores in grupo:
        print(repr(lutadores))

    print("\n\nMédicos:")
    for medicos in equipeM:
        print(repr(medicos))

    print("\n\n" + '-'*15)
    while len(grupo) > 1:
        atacante = choice(grupo)
        alvo = choice([r for r in grupo if r != atacante])
        
        print(f"{atacante.nome} ataca {alvo.nome}!")
        atacante.atacar(alvo)
        
        if alvo.vida < 0.1:
            print(f"{alvo.nome} está com pouca vida e pede ajuda médica!")
            medico = choice(equipeM)
            
            if choice([True, False]):  
                print(f"{medico.nome} atende {alvo.nome} e realiza cura!")
                medico.curar(alvo)
            else:
                print(f"{medico.nome} recusou o chamado de {alvo.nome}!")
        
        if atacante.vida < 0.1:
            print(f"{atacante.nome} está com pouca vida e pede ajuda médica!")
            medico = choice(equipeM)
            
            if choice([True, False]):  
                print(f"{medico.nome} atende {atacante.nome} e realiza cura!")
                medico.curar(atacante)
            else:
                print(f"{medico.nome} recusou o chamado de {atacante.nome}!")
        
        if alvo.vida < 0.075:
            print(f"{alvo.nome} foi eliminado!")
            grupo.remove(alvo)
        
    print(f"Vencedor do grupo: {grupo[0].nome}\n")

    print('-'*15)
    return grupo[0]

def main():
    # Criando lutadores
    lutadores = [RoboLutador(f"L{i}") for i in range(6)]
    medicos = [RoboMedico(f"M{i}") for i in range(4)]

    # Dividindo em dois grupos
    grupo1 = lutadores[:3]
    grupo2 = lutadores[3:]
    equipeM1 = medicos[:2]
    equipeM2 = medicos[2:]
    
    print("\n--- Campeonato de Robôs Lutadores ---")
    
    vencedor1 = simular_luta(grupo1, equipeM1, 'Fases_de_Grupos')
    vencedor2 = simular_luta(grupo2, equipeM2,'Fases_de_Grupos')
    
    campeao = simular_luta([vencedor1, vencedor2], medicos, 'Final')
    
    print('-'*15)
    print(f"\nO grande campeão é: {campeao.nome}!")
    
    robos = [Robo(f"R{i}") for i in range(3)]
    medicos = [RoboMedico(f"M{i}") for i in range(3)]
    lutadores = [RoboLutador(f"L{i}") for i in range(3)]    
    for _ in range(3):
        pai = choice(robos + lutadores + medicos)
        mae = choice(robos + lutadores + medicos)
        if pai != mae:
            bebe = pai + mae
            if isinstance(bebe, RoboLutador):
                lutadores.append(bebe)
            elif isinstance(bebe, RoboMedico):
                medicos.append(bebe)
            else:
                robos.append(bebe)
            print(f"{pai.nome} e {mae.nome} geraram {bebe.nome}!")
    
    # Exibindo listas finais de robôs
    print("\n--- Listas Finais de Robôs ---")
    print("Robôs:", [robo.nome for robo in robos])
    print("Lutadores:", [lutador.nome for lutador in lutadores])
    print("Médicos:", [medico.nome for medico in medicos])
    
    print("--- Fim da Simulação ---")

if __name__ == "__main__":
    main()