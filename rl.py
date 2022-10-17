import random
import ast
import time

from algorithms import *
from utils import *
import os.path

learningTable = {}
tabla = start_othello_game()
lasttable = []
alpha = 0
entrenar = True
gameResult = 0
iteraciones = 0
jugador_agente = 2
qrate = 0.0
N = 1
counter = 0


def setN(a):
    global N
    N = a


def setqRate(a):
    global qrate
    qrate = a


def reset():
    global learningTable
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    tabla = start_othello_game()


def calculateReward(tabla, jugador):
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    contrario = (jugador % 2) + 1

    result = calculate_game_result(tabla)
    if result == jugador:
        return 1.0
    elif result == contrario:
        return 0.0
    elif result == -1:
        return 0.0
    else:
        return getProbability(tabla)


def getProbability(tabla):
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    global counter
    stabla = deepcopy(tabla)
    cleanReachableStateTable(stabla)
    stabla = serializeTable(stabla)
    if stabla not in learningTable.keys():
        learningTable[stabla] = 0.5
    else:
        counter = counter + 1
    return learningTable[stabla]


def updateProbability(tablero, nextStateProb, jugador):
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    prob = calculateReward(tablero, jugador)
    prob = prob + alpha * (nextStateProb - prob)
    stabla = deepcopy(tablero)
    cleanReachableStateTable(stabla)
    learningTable[serializeTable(stabla)] = prob


def jugar(jugador):
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    prob = 0
    row = 0
    col = 0
    maxProb = -float('inf')

    for i in range(8):
        for j in range(8):
            if tabla[i][j] == jugador + 2 or tabla[i][j] == 5:
                temptable = deepcopy(tabla)
                applyMov(temptable, [i, j], jugador)
                cleanReachableStateTable(temptable)
                reachable_states_table(temptable)
                prob = calculateReward(temptable, jugador)
                if prob > maxProb:
                    maxProb = prob
                    row = i
                    col = j
                if prob == maxProb and random.randint(0, 1) == 1:
                    row = i
                    col = j
    if entrenar:
        updateProbability(tabla, maxProb, jugador)
    applyMov(tabla, [row, col], jugador)
    cleanReachableStateTable(tabla)
    reachable_states_table(tabla)

    lasttable = deepcopy(tabla)


def jugarRandom(jugador):
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    applyMov(tabla, playRandom(tabla, jugador)['mov'], jugador)
    cleanReachableStateTable(tabla)
    reachable_states_table(tabla)
    lasttable = deepcopy(tabla)


def updateAlpha(currentgame):
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    alpha = 0.5 - 0.49 * currentgame / N


def jugarVsRandom():
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    jugador = jugador_agente
    contrario = (jugador % 2) + 1

    turno = 2
    result = 0
    while result == 0:
        canp = playerCanPlay(tabla, turno)
        if canp:
            if turno == jugador:
                q = random.random()
                if q <= qrate or not entrenar:
                    jugar(jugador)
                else:
                    jugarRandom(jugador)
            else:
                applyMov(tabla, playRandom(tabla, contrario)['mov'], contrario)
                cleanReachableStateTable(tabla)
                reachable_states_table(tabla)
            result = calculate_game_result(tabla)
        turno = 2 - turno + 1
    if result != jugador and entrenar:
        updateProbability(lasttable, calculateReward(tabla, jugador), jugador)


def jugarVsAB(corte):
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    jugador = jugador_agente
    contrario = (jugador % 2) + 1

    turno = 2
    result = 0
    while result == 0:
        canp = playerCanPlay(tabla, turno)
        if canp:
            if turno == jugador:
                q = random.random()
                if q <= qrate or not entrenar:
                    jugar(jugador)
                else:
                    jugarRandom(jugador)
            else:
                applyMov(tabla, minimaxABDecision(tabla, corte, contrario, jugador)['mov'], contrario)
                cleanReachableStateTable(tabla)
                reachable_states_table(tabla)
            result = calculate_game_result(tabla)
        turno = 2 - turno + 1
    if result != jugador and entrenar:
        updateProbability(lasttable, calculateReward(tabla, jugador), jugador)

def jugarVsRL():
    global tabla
    global lasttable
    global alpha
    global entrenar
    global gameResult
    global iteraciones
    global jugador_agente
    global qrate
    global N
    jugador = jugador_agente
    contrario = (jugador % 2) + 1

    turno = 2
    result = 0
    while result == 0:
        canp = playerCanPlay(tabla, turno)
        if canp:
            if turno == jugador:
                q = random.random()
                if q <= qrate or not entrenar:
                    jugar(jugador)
                else:
                    jugarRandom(jugador)
            else:
                applyMov(tabla, playAgainsRL(tabla, contrario)['mov'], contrario)
                cleanReachableStateTable(tabla)
                reachable_states_table(tabla)
            result = calculate_game_result(tabla)
        turno = 2 - turno + 1
    if result != jugador and entrenar:
        updateProbability(lasttable, calculateReward(tabla, jugador), jugador)


def trainRL(trainingCount, qrates, player, opponent, corte):
    setN(trainingCount)
    setqRate(qrates)
    global jugador_agente
    jugador_agente = player
    start = time.time()
    loadLearningTable()
    startlen = len(learningTable)
    end = time.time()
    loadtime = end - start
    start = time.time()
    for i in range(N):
        if i % 10 == 0:
            print(i)
        reset()
        updateAlpha(i)
        if opponent == 1:
            jugarVsRandom()
        elif opponent == 3:
            jugarVsRL()
        else:
            jugarVsAB(corte)
    saveLearningTable()
    end = time.time()
    trainduration = end - start
    endlen = len(learningTable)
    return {
        "startlen": startlen,
        "loadtime": loadtime,
        "trainduration": trainduration,
        "endlen": endlen,
        "actualized_elements": counter
    }


def loadLearningTable():
    global learningTable
    global jugador_agente
    if not os.path.exists('Original.txt') and jugador_agente == 2:
        return
    elif not os.path.exists('Original2.txt') and jugador_agente == 1:
        return
    if jugador_agente == 2:
        f = open('Original.txt', 'r')
    elif jugador_agente == 1:
        f = open('Original2.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
    learningTable = ast.literal_eval(contents)


def saveLearningTable():
    global learningTable
    global jugador_agente
    if jugador_agente == 2:
        file1 = open("Original.txt", "w")
    elif jugador_agente == 1:
        file1 = open("Original2.txt", "w")
    str1 = repr(learningTable)
    file1.write(str1)
    file1.close()


def playAgainsRL(table, turno):
    global jugador_agente
    jugador_agente = turno
    loadLearningTable()
    prob = 0
    row = 0
    col = 0
    maxProb = -float('inf')

    for i in range(8):
        for j in range(8):
            if table[i][j] == turno + 2 or table[i][j] == 5:
                temptable = deepcopy(table)
                applyMov(temptable, [i, j], turno)
                cleanReachableStateTable(temptable)
                reachable_states_table(temptable)
                prob = calculateReward(temptable, turno)
                if prob > maxProb:
                    maxProb = prob
                    row = i
                    col = j
                if prob == maxProb and random.randint(0, 1) == 1:
                    row = i
                    col = j
    if entrenar:
        updateProbability(tabla, maxProb, turno)

    return {'mov': [row, col], 'nodos': 0}


# x = trainRL(trainingCount=10, qrates=0.7, player=1, opponent=2)
# print(len(x))
print(counter)
