from flask import Flask, render_template,redirect, jsonify
import backend as backend

app = Flask(__name__)


@app.route('/')
def hello():
    backend.createTables()
    metricTable = backend.getMetricTable()
    valueDefTable = backend.getValueDefinitionTable()
    return render_template('index.html',details=metricTable,valueDefs = valueDefTable)

@app.route("/uploadCSV")
def upload():
    backend.createTables()
    backend.CSVtoSQL()
    return redirect("/")

@app.route("/getMerticTable",methods=["GET"])
def getMetricTable():
    metricTable = backend.getMetricTable()
    return jsonify(metricTable)

@app.route("/getValueDefTable",methods=["GET"])
def getValueDefTable():
    valueDefTable = backend.getValueDefinitionTable()
    return jsonify(valueDefTable)

@app.route("/emptyDatabase",methods=["GET"])
def emptyDatabase():
    deleted = backend.deleteDatabase()
    return redirect("/")

if __name__ == '__main__':  
   app.run(debug = True)  