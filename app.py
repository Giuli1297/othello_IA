from flask import Flask, render_template, request
from game import game

app = Flask(__name__)

algorithms = {
    'minimax': 1,
    'alphabeta': 2,
    'reinforcement_learning': 3
}


def crearTablero(n):
    board = [[0 for x in range(n)] for y in range(n)]

    coord1 = int((n/2)-1)
    coord2 = int((n/2))

    board[coord1][coord1] = 1
    board[coord1][coord2] = 2
    board[coord2][coord1] = 2
    board[coord2][coord2] = 1

    return board


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(request.form)
        algorithm1 = int(request.form['algoritmo1'])
        algorithm2 = int(request.form['algoritmo2'])
        corte1 = int(request.form['corte'])
        corte2 = int(request.form['corte2'])

        if algorithm1 == algorithm2:
            return render_template('index.html', error='Los algoritmos deben ser diferentes')

        result = game(algorithm1, algorithm2, corte1, corte2)
        print(result)
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

    # if request.method == 'GET':
    #     print(request.args.get("codigo"))
    #     return game(1, 2, 1, 1)
    # elif request.method == 'POST':
    #     return {"message": "post"}


if __name__ == '__main__':
    app.run()
