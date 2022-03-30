from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import threading
import time

DB_NAME = "lamps.db"
app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = 'hjshjhdjahkjshkjdhjs'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

#classe que representa uma tabela do banco de dados
class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(10), nullable=False)

    def __init__(self, id, name, state):
        self.id = id
        self.name = name
        self.state = state

"""
db.create_all()

sala = Devices(1, "sala", "False")
cozinha = Devices(2, "cozinha", "False")
quarto = Devices(3, "quarto", "False")
banheiro = Devices(4, "banheiro", "False")

db.session.add(sala)
db.session.add(cozinha)
db.session.add(quarto)
db.session.add(banheiro)


db.session.commit()
"""
#tuplas do banco de dados que representam as lampadas
sala = Devices.query.filter_by(id=1).first()
cozinha = Devices.query.filter_by(id=2).first()
quarto = Devices.query.filter_by(id=3).first()
banheiro = Devices.query.filter_by(id=4).first()

#pagina raiz do site
@app.route("/")
def control_panel_route():
    global app, db
    state = []
    db.init_app(app)
    #capitura os status das luzes gravadas no banco de dados
    for i in range(4):
        var = Devices.query.filter_by(id=i+1).first()
        state.append(var.state)
    return render_template('control.html',
                           sala=state[0],
                           cozinha=state[1],
                           quarto=state[2],
                           banheiro=state[3])

#pagina para alterar o banco de dados quando um botão é pressionado
@app.route("/comodos/<string>", methods=["POST", "GET"])
def sala_edit(string):
    global app, db
    db.init_app(app)
    i = 0
    if (string == "sala"):
        i = 1
    elif (string == "cozinha"):
        i = 2
    elif (string == "quarto"):
        i = 3
    elif (string == "banheiro"):
        i = 4
    var = Devices.query.filter_by(id=i).first()
    if(var.state == "False"):
        setattr(var, 'state', "True")
        db.session.commit()
    elif (var.state == "True"):
        setattr(var, 'state', "False")
        db.session.commit()
    return redirect("/")

#pagina para ler o status de uma tupla no banco de dados
@app.route("/state/<string>", methods=["POST", "GET"])
def sala_state(string):
    global db, app
    db.init_app(app)
    i = 0
    if(string == "sala"):
        i = 1
    elif(string == "cozinha"):
        i = 2
    elif (string == "quarto"):
        i = 3
    elif (string == "banheiro"):
        i = 4
    var = Devices.query.filter_by(id=i).first()
    return var.state


if __name__ == "__main__":
    app.run()

