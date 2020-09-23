import os
import pymongo
from pymongo import MongoClient
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!!!"

@app.route("/getDatabases")
def getDatabases(): 
  # Se crea la conexión con MongoDB
  db_host = str(os.getenv("MONGO_SVC_SERVICE_HOST","db"))
  db_port = 27017
  cn = pymongo.MongoClient(db_host ,db_port)
  databases= cn.list_database_names()
  cn.close()
  return "Lista de bases de datos: %s " %(databases)
  
@app.route("/test")
def test():
  return app.send_static_file('App/test.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
