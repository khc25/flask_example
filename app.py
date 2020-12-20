from flask import Flask
app = Flask(__name__)
from flask import request
import psycopg2

conn = psycopg2.connect("dbpostgres://obbyumtp:McdTVFblMMvaFMEgp9FaC44jS7j7ZwX1@suleiman.db.elephantsql.com:5432/obbyumtp")
cur = conn.cursor()

@app.route('/post', methods=["POST"])
def hello_world():
    username = request.form["username"]
    password = request.form["password"]
    cur.excute("INSERT INTO test (username, password) VALUES (%s, %s)",(username, password))
    return "Success"

@app.route('/', methods=["GET"])
def get():
    cur.excute("SELECT * FROM test")