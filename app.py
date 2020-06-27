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


@app.route('/slangs/<word>/<meaning>')
def slangs(word , meaning):
    print("Esto es prueba de que {} significa : {}!".format(word,meaning))
    if word =="Mopri" and meaning =="primo":
        return url_for('index')
    else :
        return "kombawa"
@app.route("/new_word/<word>/<meaning>")
def new_word(word , meaning):
    db.db.collection.insert_one({"word":word,"meaning" :meaning})
    return "Se pudo añadir {} correctamente con su significado{}".format(word,meaning)

@app.route("/edit/<word>/<new_meaning>")
def edit(word , new_meaning):
    word.strip()
    new_meaning.strip()
    collection.update_one({"Word":word} , {"$set":new_meaning})
    return "La palabra {} se ha actualizado! el nuevo significado es{}".format(word , new_meaning)

@app.route("/delete/<word>")
def delete(word):
    word.strip()
    collection.delete_one({"Word":word})        

#so far the show option was only available while only using python..... translation to flask is still needed
@app.route("/show")
def show():
    words = collection.find()
    return 



if __name__ == "__main__":
    app.run(debug= True, port= 8000)