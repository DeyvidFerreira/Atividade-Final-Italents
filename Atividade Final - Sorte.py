import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play():
    return random.randint(1, 6)

def input_number(text,error,inteiro):
    while True:
        try:
            entrada = input(text)
            number = float(entrada)
            if inteiro:
                number = int(number)
            elif number % 1 == 0:
                number = int(number)
            return(number)
        except ValueError:
            clear()
            print(error)

clear()

# inicio do código
print("Vamo jogar um jogo de sorte?\n")
jogadores = []

# Entradas de dados
quant_jogadores = input_number("Quantas pessoas Irão participar: ", "Não entendi, tente utilizar numeros inteiros.",True)

for jogador in range(1,quant_jogadores + 1):
    nome = input(f"Digite o nome do jogador {jogador}: ")
    jogadores.append({"nome": nome, "jogadas": [], "vitorias": 0})
    clear()

quant_rodadas = input_number("Quantas Rodadas serão: ","Poderia repetir?",True)

clear()

# Inicio das rodadas
for rodada in range(1,quant_rodadas + 1):
    print(f"\nRodada {rodada}:")

    resultados_rodada = [play() for _ in range(quant_jogadores)]
    maior_pontuacao = max(resultados_rodada)

    for i, player in enumerate(jogadores):
        player["jogadas"].append(resultados_rodada[i])
        print(f"{player["nome"]} tirou {resultados_rodada[i]}")

        if resultados_rodada[i] ==  maior_pontuacao:
                player["vitorias"] += 1


# Resultados
print("\n")
for player in jogadores:
    print(player['nome']," Ganhou ",player['vitorias']," rodadas")

jogadores.sort(key=lambda x: x['vitorias'], reverse=True)

if len(jogadores) > 1 and jogadores[0]['vitorias'] == jogadores[1]['vitorias']:
    print("\nHouve um empate!")
else:
    print(f"\nO vencedor é {jogadores[0]['nome']}!")