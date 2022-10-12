import random
import time


from utils import *
from algorithms import minimaxDecision, minimaxABDecision


def playInSomeWay(table, cod, iterations, player, opponent):
    mov = 0
    if cod == 1:
        mov = minimaxDecision(table, iterations, player, opponent)
    elif cod == 2:
        mov = playRandom(table, player)
    elif cod == 3:
        mov = minimaxABDecision(table, iterations, player, opponent)
    return mov


def game(algorithm1, algorithm2, algoritm1_level, algorithm2_level):
    table = start_othello_game()
    cod1 = algorithm1
    cod2 = algorithm2
    nodos_expandidos_player1 = []
    nodos_expandidos_player2 = []
    tiempo_player1 = []
    tiempo_player2 = []
    result = 0
    counter = 1
    while result == 0:
        turno = counter % 2 + 1
        counter = counter + 1
        if turno == 2:
            if playerCanPlay(table, 2):
                start = time.time()
                movandnodos = playInSomeWay(table, cod=cod1, iterations=algoritm1_level, player=2, opponent=1)
                end = time.time()
                mov = movandnodos["mov"]
                nodos_expandidos_player1.append(movandnodos["nodos"])
                tiempo_player1.append(end-start)
                applyMov(table, mov, turno)
                cleanReachableStateTable(table)
                reachable_states_table(table)
        else:
            if playerCanPlay(table, 1):
                start = time.time()
                movandnodos = playInSomeWay(table, cod=cod2, iterations=algorithm2_level, player=1, opponent=2)
                end = time.time()
                mov = movandnodos["mov"]
                nodos_expandidos_player2.append(movandnodos["nodos"])
                tiempo_player2.append(end-start)
                applyMov(table, mov, turno)
                cleanReachableStateTable(table)
                reachable_states_table(table)
        result = calculate_game_result(table)
    # print(table)
    print(max(nodos_expandidos_player1))
    print(max(nodos_expandidos_player2))
    # print(tiempo_player1)
    # print(tiempo_player2)
    return {"ganador": result,
            "tabla": table,
            "nodos_expandidos_player1": nodos_expandidos_player1,
            "nodos_expandidos_player2": nodos_expandidos_player2,
            "tiempos_player1": tiempo_player1,
            "tiempos_player2": tiempo_player2}


def playRandom(table, player):
    plays = []
    for i in range(8):
        for j in range(8):
            if table[i][j] == player + 2 or table[i][j] == 5:
                plays.append([i, j])
    return {"mov": random.choice(plays),
            "nodos": 1}


