from flask import Flask, render_template, request
from game import *
from rl import trainRL
from utils import *

app = Flask(__name__)

algorithms = {
    'minimax': 1,
    'alphabeta': 2,
    'reinforcement_learning': 3
}

dictionaryLN = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST' and int(request.form['entrenar']) == 0:
        algorithm1 = int(request.form['algoritmo1'])
        algorithm2 = int(request.form['algoritmo2'])
        corte1 = int(request.form['corte'])
        corte2 = int(request.form['corte2'])

        # if algorithm1 == algorithm2:
        #     return render_template('index.html', error='Los algoritmos deben ser diferentes')

        if algorithm1 == 0 and algorithm2 != 0:
            algoritmo = algorithm2
            table = start_othello_game()
            stable = serializeTable(table)
            cleanReachableStateTableForPlayer(table, 1)
            print(table)
            jugandocontext = {
                'table': table,
                'stable': stable,
                'corte': corte2,
                'algoritmo': algoritmo,
                'jugador': 2,
                'jugadas': jugadasgen(table, 2)
            }
            return render_template('index.html', context=jugandocontext)
        elif algorithm1 != 0 and algorithm2 == 0:
            algoritmo = algorithm1
            table = start_othello_game()
            mov_nod = playInSomeWay(table, algorithm1, corte1, player=2, opponent=1)
            mov = mov_nod['mov']
            applyMov(table, mov, 2)
            cleanReachableStateTable(table)
            reachable_states_table(table)
            stable = serializeTable(table)
            cleanReachableStateTableForPlayer(table, opponent=2)
            print(table)
            jugandocontext = {
                'table': table,
                'stable': stable,
                'corte': corte1,
                'algoritmo': algoritmo,
                'jugador': 1,
                'jugadas': jugadasgen(table, 1)
            }
            return render_template('index.html', context=jugandocontext)
        if algorithm1 == 100:
            table = deserializeTable(request.form['stable'])
            corte = int(request.form['corte'])
            jugador = int(request.form['jugador'])
            fila = dictionaryLN[request.form['fila-columna'][0]]
            columna = int(request.form['fila-columna'][1])-1
            algoritmo = int(request.form['algoritmo'])
            if calculate_game_result(table) == 0:
                applyMov(table, [fila, columna], jugador)
                cleanReachableStateTable(table)
                reachable_states_table(table)
                if playerCanPlay(table, jugador % 2 + 1):
                    mov_nod = playInSomeWay(table, algoritmo, corte, jugador % 2 + 1, jugador)
                    mov = mov_nod['mov']
                    applyMov(table, mov, jugador % 2 + 1)
                    cleanReachableStateTable(table)
                    reachable_states_table(table)
                while not playerCanPlay(table, jugador):
                    if calculate_game_result(table) != 0:
                        stable = 0
                        return render_template('index.html', context={
                            'table': table,
                            'stable': stable,
                            'corte': corte,
                            'algoritmo': algoritmo,
                            'jugador': jugador,
                            'ganador': calculate_game_result(table),
                            'jugadas': jugadasgen(table, jugador)
                        })
                    mov_nod = playInSomeWay(table, algoritmo, corte, jugador % 2 + 1, jugador)
                    mov = mov_nod['mov']
                    applyMov(table, mov, jugador % 2 + 1)
                    cleanReachableStateTable(table)
                    reachable_states_table(table)
                stable = serializeTable(table)
                cleanReachableStateTableForPlayer(table, opponent=jugador % 2 + 1)
                jugandocontext = {
                    'table': table,
                    'stable': stable,
                    'corte': corte,
                    'algoritmo': algoritmo,
                    'jugador': jugador,
                    'jugadas': jugadasgen(table, jugador)
                }
                return render_template('index.html', context=jugandocontext)
            else:
                stable = 0
                return render_template('index.html', context={
                    'table': table,
                    'stable': stable,
                    'corte': corte,
                    'algoritmo': algoritmo,
                    'jugador': jugador,
                    'ganador': calculate_game_result(table),
                    'jugadas': jugadasgen(table, jugador)
                })
        result = game(algorithm1, algorithm2, corte1, corte2)
        # Average of a list
        nodos_expandidos_player1_promedio = sum(
            result['nodos_expandidos_player1']) / len(result['nodos_expandidos_player1'])
        nodos_expandidos_player2_promedio = sum(
            result['nodos_expandidos_player2']) / len(result['nodos_expandidos_player2'])

        # max of lkist
        nodos_expandidos_player1_max = max(result['nodos_expandidos_player1'])
        nodos_expandidos_player2_max = max(result['nodos_expandidos_player2'])

        tiempo_total_algoritmo_1 = sum(result['tiempos_player1'])
        tiempo_total_algoritmo_2 = sum(result['tiempos_player2'])
        result = {
            'ganador': result['ganador'],
            'tabla': result['tabla'],
            'nodos_expandidos_algoritmo_1_promedio': nodos_expandidos_player1_promedio,
            'nodos_expandidos_algoritmo_2_promedio': nodos_expandidos_player2_promedio,
            'nodos_expandidos_algoritmo_1_max': nodos_expandidos_player1_max,
            'nodos_expandidos_algoritmo_2_max': nodos_expandidos_player2_max,
            'tiempo_promedio1': tiempo_total_algoritmo_1/len(result['tiempos_player1']),
            'tiempo_promedio2': tiempo_total_algoritmo_2 / len(result['tiempos_player2']),
            'tiempo_total_algoritmo_1': tiempo_total_algoritmo_1,
            'tiempo_total_algoritmo_2': tiempo_total_algoritmo_2
        }

        if algorithm1 == 1:
            algorithm1 = 'MiniMax'
        elif algorithm1 == 2:
            algorithm1 = 'Random'
        elif algorithm1 == 3:
            algorithm1 = 'AlphaBeta'
        elif algorithm1 == 4:
            algorithm1 = 'Reinforcement Learning'

        if algorithm2 == 1:
            algorithm2 = 'MiniMax'
        elif algorithm2 == 2:
            algorithm2 = 'Random'
        elif algorithm2 == 3:
            algorithm2 = 'AlfaBeta'
        elif algorithm2 == 4:
            algorithm2 = 'Reinforcement Learning'

        if result['ganador'] == 1:
            result['ganador'] = "Blanco"
        elif result['ganador'] == 2:
            result['ganador'] = "Negro"

        context = {
            'result': result,
            'algoritmo1': algorithm1,
            'algoritmo2': algorithm2,
            'corte1': corte1,
            'corte2': corte2,
        }
        return render_template('index.html', **context)

    elif request.method == 'POST' and int(request.form['entrenar']) == 1:
        opponent = int(request.form['algoritmo'])
        player = int(request.form['jugador'])
        corte = int(request.form['corte'])
        pruebas = int(request.form['pruebas'])
        qrate = float(request.form['qrate'])
        trainRL(pruebas, qrate, player, opponent, corte)
        context = {
            'msj': 'Entrenado correctamente'
        }
        return render_template('index.html', **context)


def cleanReachableStateTableForPlayer(table, opponent):
    for i in range(8):
        for j in range(8):
            if table[i][j] == opponent + 2:
                table[i][j] = 0



def jugadasgen(table, jugador):
    jugadas = []
    dictionary = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
    for i in range(8):
        for j in range(8):
            if table[i][j] == jugador + 2 or table[i][j] == 5:
                jugadas.append(str(dictionary[i]) + str(j+1))
    return jugadas


if __name__ == '__main__':
    app.run()
