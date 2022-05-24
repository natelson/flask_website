from flask import Flask, render_template, request, redirect, session, flash, url_for
from game import Game
app = Flask(__name__)
app.secret_key = 'banana'

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
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login'))

    return render_template('newgame.html', title='New Game')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authentication', methods=['POST',])
def authentication():
    if request.form:
        if 'master' == request.form['password']:
            session['logged_user'] = request.form['login']
            flash('Welcome ' + request.form['login'])
            return redirect(url_for('index'))
        else:
            flash('Try again,  ' + request.form['login'])
            return redirect(url_for('login'))


@app.route('/create_game_post', methods=['POST',])
def create_game_post():
    if request.form:
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']

        game = Game(name, category, console)
        games_list.append(game)

        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Desconected')
    return redirect(url_for('login'))

app.run(debug=True)