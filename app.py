from flask import Flask, render_template, jsonify, request
from game import game

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'GET':
        print(request.args.get("codigo"))
        return game(1, 2, 1, 1)
    elif request.method == 'POST':
        return {"message": "post"}


if __name__ == '__main__':
    app.run()
