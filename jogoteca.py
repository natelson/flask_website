from flask import Flask, render_template, request, redirect
from game import Game
app = Flask(__name__)

game1 = Game('Super Mario', 'Adventure', 'NES')
game2 = Game('HALO', 'Action', 'XBOX')
game3 = Game('Nascar', 'Cars', 'PS4')
games_list = [game1, game2, game3]

@app.route('/')
def index():
    #Jinja2
    return render_template('list.html', title='Games', games_list=games_list)

@app.route('/new')
def create_game():
    return render_template('newgame.html', title='New Game')

@app.route('/create_game_post', methods=['POST',])
def create_game_post():
    if request.form:
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']

        game = Game(name, category, console)
        games_list.append(game)

        return redirect('/')

app.run(debug=True)