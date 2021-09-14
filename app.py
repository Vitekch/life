from flask import Flask
from flask import render_template
from game_of_life import GameOfLife

app=Flask(__name__)

@app.route('/')
def index():
    GameOfLife(25,25)
    return render_template('index.html')

@app.route('/life')
def life():
    game=GameOfLife()
    
    game.form_new_generation()
    game.counter+=1
    return render_template('life.html',game=game)

if(__name__=='__main__'):
    app.run(host='0.0.0.0',port=5000)
