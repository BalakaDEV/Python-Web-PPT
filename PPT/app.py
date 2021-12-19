#Imports
from flask import Flask, render_template, redirect, request
import secrets
import random
app = Flask(__name__)

#Conections
@app.route('/')
def index ():
    return render_template("index.html")

@app.route('/sobre')
def sobre ():
    return render_template("sobre.html")

@app.route('/contato')
def contato ():
    return render_template("contato.html")


#Game Body
weapons = ['Pedra', 'Papel', 'Tesoura']


@app.route("/Pedra", methods=["POST"])
def Pedra():
    possibilities = {
    'Pedra': 'Pedra Empatou.',
    'Papel': 'Papel ganhou de Pedra.(Perdeu)',
    'Tesoura': 'Pedra ganhou de Tesoura.(Ganhou)'
    }
    
    weapon = random.choices(weapons)[0]
    message = possibilities[weapon]
    resultado = message
    return render_template("index.html", msg=resultado, comp=weapon)


@app.route("/Papel", methods=["POST"])
def Papel():   
    possibilities = {
    'Pedra': 'Papel ganhou de pedra.(Ganhou)',
    'Papel': 'Papel Empatou.',
    'Tesoura': 'Tesoura ganhou de papel.(Perdeu)'
    }

    weapon = random.choices(weapons)[0]
    message = possibilities[weapon]
    resultado = message
    return render_template("index.html", msg=resultado, comp=weapon)


@app.route("/Tesoura", methods=["POST"])
def Tesoura():   
    possibilities = {
    'Pedra': 'Pedra ganhou de tesoura.(Perdeu)',
    'Papel': 'Tesoura ganhou de papel.(Ganhou)',
    'Tesoura': 'Tesoura Empatou.'
    }

    weapon = random.choices(weapons)[0]
    message = possibilities[weapon]
    resultado = message
    return render_template("index.html", msg=resultado, comp=weapon)


#Debug
if __name__ == "__main__":
    app.run(debug=True)
