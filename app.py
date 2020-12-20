from flask import Flask
app = Flask(__name__)
from flask import request
import psycopg2
import urlparse

result = urlparse.urlparse("dbpostgres://obbyumtp:McdTVFblMMvaFMEgp9FaC44jS7j7ZwX1@suleiman.db.elephantsql.com:5432/obbyumtp")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
conn = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname
)
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