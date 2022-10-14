from utils import *
from copy import deepcopy
import random
node_counter = 0


def minimaxDecision(table, iterations, player, opponenent):
    playTable = deepcopy(table)
    global node_counter
    node_counter = 0
    returnValue = minimaxValue(playTable, player, opponenent, iterations, 1, player)[0]
    return {"mov": returnValue, "nodos": node_counter}


def minimaxABDecision(table, iterations, player, opponenent):
    playTable = deepcopy(table)
    global node_counter
    node_counter = 0
    returnValue = minimaxABValue(playTable, player, opponenent, iterations, 1, player, -float("inf"), float("inf"))[0]
    return {"mov": returnValue, "nodos": node_counter}


def maxPlay(plays):
    # print(plays)
    max_play = plays[0]
    for play in plays:
        if play[1] > max_play[1]:
            max_play = play
    return max_play


def minPlay(plays):
    # print(plays)
    min_play = plays[0]
    for play in plays:
        if play[1] < min_play[1]:
            min_play = play
    return min_play


def minimaxValue(table, maxplayer, minplayer, iterations, it_counter, turno):
    global node_counter
    node_counter = node_counter + 1
    turno = turno
    if turno == maxplayer and not playerCanPlay(table, turno):
        turno = minplayer
    elif turno == minplayer and not playerCanPlay(table, turno):
        turno = maxplayer

    if calculate_game_result(table) != 0 or it_counter == iterations + 1:
        return utilityFunction(table, maxplayer, minplayer)
    elif turno == maxplayer:
        jugadas = []
        for i in range(8):
            for j in range(8):
                if table[i][j] == maxplayer + 2 or table[i][j] == 5:
                    tempTable = deepcopy(table)
                    applyMov(tempTable, [i, j], maxplayer)
                    cleanReachableStateTable(tempTable)
                    reachable_states_table(tempTable)
                    value = minimaxValue(tempTable, maxplayer, minplayer, iterations, it_counter + 1, minplayer)
                    if type(value) == list:
                        jugadas.append([[i, j], value[1]])
                    else:
                        jugadas.append([[i, j], value])
        return maxPlay(jugadas)
    else:
        jugadas = []
        for i in range(8):
            for j in range(8):
                if table[i][j] == minplayer + 2 or table[i][j] == 5:
                    tempTable = deepcopy(table)
                    applyMov(tempTable, [i, j], minplayer)
                    cleanReachableStateTable(tempTable)
                    reachable_states_table(tempTable)
                    value = minimaxValue(tempTable, maxplayer, minplayer, iterations, it_counter + 1, maxplayer)
                    if type(value) == list:
                        jugadas.append([[i, j], value[1]])
                    else:
                        jugadas.append([[i, j], value])
        return minPlay(jugadas)


def minimaxABValue(table, maxplayer, minplayer, iterations, it_counter, turno, alfa, beta):
    global node_counter
    node_counter = node_counter + 1
    turno = turno
    if turno == maxplayer and not playerCanPlay(table, turno):
        turno = minplayer
    elif turno == minplayer and not playerCanPlay(table, turno):
        turno = maxplayer

    alfahere = alfa
    betahere = beta

    if calculate_game_result(table) != 0 or it_counter == iterations + 1:
        return utilityFunction(table, maxplayer, minplayer)
    elif turno == maxplayer:
        jugadas = []
        for i in range(8):
            for j in range(8):
                if table[i][j] == maxplayer + 2 or table[i][j] == 5:
                    tempTable = deepcopy(table)
                    applyMov(tempTable, [i, j], maxplayer)
                    cleanReachableStateTable(tempTable)
                    reachable_states_table(tempTable)
                    value = minimaxABValue(tempTable, maxplayer, minplayer, iterations, it_counter + 1, minplayer,
                                           alfahere, betahere)
                    if type(value) == list:
                        jugadas.append([[i, j], value[1]])
                        hvalue = value[1]
                    else:
                        jugadas.append([[i, j], value])
                        hvalue = value
                    if hvalue > alfahere:
                        alfahere = hvalue
                    if betahere <= alfahere:
                        return maxPlay(jugadas)
        return maxPlay(jugadas)
    else:
        jugadas = []
        for i in range(8):
            for j in range(8):
                if table[i][j] == minplayer + 2 or table[i][j] == 5:
                    tempTable = deepcopy(table)
                    applyMov(tempTable, [i, j], minplayer)
                    cleanReachableStateTable(tempTable)
                    reachable_states_table(tempTable)
                    value = minimaxABValue(tempTable, maxplayer, minplayer, iterations, it_counter + 1, maxplayer,
                                           alfahere, betahere)
                    if type(value) == list:
                        jugadas.append([[i, j], value[1]])
                        hvalue = value[1]
                    else:
                        jugadas.append([[i, j], value])
                        hvalue = value
                    if hvalue < betahere:
                        betahere = hvalue
                    if betahere <= alfahere:
                        return minPlay(jugadas)
        return minPlay(jugadas)


def utilityFunction(table, player, opponent):
    tableHeuristic = 0
    playerPieces = 0
    opponentPieces = 0
    playerFrontPieces = 0
    opponentFrontPieces = 0
    piecesHeuristic = 0
    frontPiecesHeuristic = 0
    cornerPiecesHeuristic = 0
    cornerClosenessHeuristic = 0
    movilityHeuristic = 0
    adjacentCornerX = [-1, -1, 0, 1, 1, 1, 0, -1]
    adjacentCornerY = [0, 1, 1, 1, 0, -1, -1, -1]

    hMatrix = [[20, -3, 11, 8, 8, 11, -3, 20],
               [-3, -7, -4, 1, 1, -4, -7, -3],
               [11, -4, 2, 2, 2, 2, -4, 11],
               [8, 1, 2, -3, -3, 2, 1, 8],
               [8, 1, 2, -3, -3, 2, 1, 8],
               [11, -4, 2, 2, 2, 2, -4, 11],
               [-3, -7, -4, 1, 1, -4, -7, -3],
               [20, -3, 11, 8, 8, 11, -3, 20]]

    # Diferencia de piezas, piezas en frontera y valor sumado de la matriz heuristica

    for i in range(8):
        for j in range(8):
            if table[i][j] == player:
                tableHeuristic = tableHeuristic + hMatrix[i][j]
                playerPieces = playerPieces + 1
            elif table[i][j] == opponent:
                tableHeuristic = tableHeuristic - hMatrix[i][j]
                opponentPieces = opponentPieces + 1
            if table[i][j] != 1 and table != 2:
                for k in range(8):
                    x = i + adjacentCornerX[k]
                    y = i + adjacentCornerY[k]
                    if 0 <= x < 8 and 0 <= y < 8 and table[x][y] != 1 and table[x][y] != 2:
                        if table[i][j] == player:
                            playerFrontPieces = playerFrontPieces + 1
                        else:
                            opponentFrontPieces = opponentFrontPieces + 1
                        break

    if playerPieces > opponentPieces:
        piecesHeuristic = (100.0 * playerPieces) / (playerPieces + opponentPieces)
    elif opponentPieces > playerPieces:
        piecesHeuristic = -(100.0 * playerPieces) / (playerPieces + opponentPieces)
    else:
        piecesHeuristic = 0

    if playerFrontPieces > opponentFrontPieces:
        frontPiecesHeuristic = (100.0 * playerFrontPieces) / (playerFrontPieces + opponentFrontPieces)
    elif opponentFrontPieces > playerFrontPieces:
        frontPiecesHeuristic = -(100.0 * playerFrontPieces) / (playerFrontPieces + opponentFrontPieces)
    else:
        frontPiecesHeuristic = 0

    # Ocupacion de Esquinas

    playerPieces = opponentPieces = 0
    if table[0][0] == player:
        playerPieces = playerPieces + 1
    elif table[0][0] == opponent:
        opponentPieces = opponentPieces + 1
    if table[0][7] == player:
        playerPieces = playerPieces + 1
    elif table[0][7] == opponent:
        opponentPieces = opponentPieces + 1
    if table[7][0] == player:
        playerPieces = playerPieces + 1
    elif table[7][0] == opponent:
        opponentPieces = opponentPieces + 1
    if table[7][7] == player:
        playerPieces = playerPieces + 1
    elif table[7][7] == opponent:
        opponentPieces = opponentPieces + 1

    cornerPiecesHeuristic = 25 * (playerPieces - opponentPieces)

    # Ocupacions de cercania a esquinas

    playerPieces = opponentPieces = 0;
    if table[0][0] != 1 and table[0][0] != 2:
        if table[0][1] == player:
            playerPieces = playerPieces + 1
        elif table[0][1] == opponent:
            opponentPieces = opponentPieces + 1
        if table[1][1] == player:
            playerPieces = playerPieces + 1
        elif table[1][1] == opponent:
            opponentPieces = opponentPieces + 1
        if table[1][0] == player:
            playerPieces = playerPieces + 1
        elif table[1][0] == opponent:
            opponentPieces = opponentPieces + 1

    if table[0][7] != 1 and table[0][7] != 2:
        if table[0][6] == player:
            playerPieces = playerPieces + 1
        elif table[0][6] == opponent:
            opponentPieces = opponentPieces + 1
        if table[1][6] == player:
            playerPieces = playerPieces + 1
        elif table[1][6] == opponent:
            opponentPieces = opponentPieces + 1
        if table[1][7] == player:
            playerPieces = playerPieces + 1
        elif table[1][7] == opponent:
            opponentPieces = opponentPieces + 1

    if table[7][0] != 1 and table[7][0] != 2:
        if table[6][0] == player:
            playerPieces = playerPieces + 1
        elif table[6][0] == opponent:
            opponentPieces = opponentPieces + 1
        if table[6][1] == player:
            playerPieces = playerPieces + 1
        elif table[6][1] == opponent:
            opponentPieces = opponentPieces + 1
        if table[7][1] == player:
            playerPieces = playerPieces + 1
        elif table[7][1] == opponent:
            opponentPieces = opponentPieces + 1

    if table[7][7] != 1 and table[7][7] != 2:
        if table[7][6] == player:
            playerPieces = playerPieces + 1
        elif table[7][6] == opponent:
            opponentPieces = opponentPieces + 1
        if table[6][6] == player:
            playerPieces = playerPieces + 1
        elif table[6][6] == opponent:
            opponentPieces = opponentPieces + 1
        if table[6][7] == player:
            playerPieces = playerPieces + 1
        elif table[6][7] == opponent:
            opponentPieces = opponentPieces + 1

    cornerClosenessHeuristic = -12.5 * (playerPieces - opponentPieces)

    # Mobilidad

    playerMovility = moves_quantity(player, table);
    opponentMovility = moves_quantity(opponent, table);
    if playerMovility > opponentMovility:
        movilityHeuristic = (100.0 * playerMovility) / (playerMovility + opponentMovility)
    elif playerMovility < opponentMovility:
        movilityHeuristic = -(100.0 * opponentMovility) / (playerMovility + opponentMovility)
    else:
        movilityHeuristic = 0

    heuristicFinalValue = (10 * piecesHeuristic) + (801.724 * cornerPiecesHeuristic) + \
                          (382.026 * cornerClosenessHeuristic) + (78.922 * movilityHeuristic) + \
                          (74.396 * frontPiecesHeuristic) + (10 * tableHeuristic)
    return heuristicFinalValue


def playRandom(table, player):
    plays = []
    for i in range(8):
        for j in range(8):
            if table[i][j] == player + 2 or table[i][j] == 5:
                plays.append([i, j])
    return {"mov": random.choice(plays),
            "nodos": 1}
