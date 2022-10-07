import random

from utils import *
from algorithms import minimaxDecision


def playInSomeWay(table, cod, iterations, player, opponent):
    mov = 0
    if cod == 1:
        mov = minimaxDecision(table, iterations, player, opponent)
    elif cod == 2:
        mov = playRandom(table, player)
    return mov


def game():
    table = start_othello_game()
    cod1 = 1
    cod2 = 2
    result = 0
    counter = 1
    while result == 0:
        turno = counter % 2 + 1
        counter = counter + 1
        if turno == 2:
            if playerCanPlay(table, 2):
                mov = playInSomeWay(table, cod=cod1, iterations=1, player=2, opponent=1)
                applyMov(table, mov, turno)
                cleanReachableStateTable(table)
                reachable_states_table(table)
        else:
            if playerCanPlay(table, 1):
                mov = playInSomeWay(table, cod=cod2, iterations=1, player=1, opponent=2)
                applyMov(table, mov, turno)
                cleanReachableStateTable(table)
                reachable_states_table(table)
        result = calculate_game_result(table)
    print(table)
    return result


def playRandom(table, player):
    plays = []
    for i in range(8):
        for j in range(8):
            if table[i][j] == player + 2 or table[i][j] == 5:
                plays.append([i, j])
    return random.choice(plays)


print(game())
