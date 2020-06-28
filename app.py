from flask import Flask 
from flask import request
from flask import render_template , url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo
client = MongoClient("mongodb+srv://josel12:passsword@cluster0-rytv6.mongodb.net/Slangs?retryWrites=true&w=majority")
db = client["Slangs"]
collection = db["slangs"]

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/saluda')
def saludar():
    return "Kombawa"


@app.route("/new_word", methods = ['POST'])
def new_word():
    if request.method == 'POST':
        word = request.form['word']
        meaning = request.form['meaning']
        db.slangs.insert_one({"word":word,"meaning" :meaning})
        return render_template("Agregar.html",word = word, meaning = meaning)


@app.route("/editar", methods = ['POST'])
def editar():
    if request.method =='POST':
        word = request.form['word']
        new_meaning = request.form['new_mean']
        db.slangs.find_one_and_update(
            {"Word" :word} ,
            {"$set":{"meaning": new_meaning}})
        return render_template("editar.html", word = word)
@app.route("/eliminar" , methods =['POST'])
def eliminar():
    if request.method == 'POST':
        word = request.form['word']
        db.slangs.delete_one({"Word" :word})
        return render_template("eliminar.html", word = word)
      

#so far the show option was only available while only using python..... translation to flask is still needed
@app.route("/lista")
def lista():
    if request.method == 'GET':
        lista = db.slangs.find({},{"_id" :0,"word":1,"meaning":1})
        return render_template("Lista.html", result = lista)
if __name__ == "__main__":
    app.run(debug= True)