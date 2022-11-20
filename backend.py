import pandas as pd
import sqlite3
import configparser
import os

# Fucntion to read the dbname and CSV name from configs.ini
def readConf():
    config = configparser.ConfigParser()
    config.read("conf/configs.ini")
    csv = config['fileDetails']['CSV']
    dbName = config['fileDetails']['dbName']
    return {"csvName": csv, "dbName": dbName}

conf = readConf()

# The following function creates both the tables and checks if they already exist
def createTables():
    conn = sqlite3.connect(conf['dbName'])
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS metric (id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT NOT NULL UNIQUE, description TEXT NOT NULL) ''')
    c.execute('''CREATE TABLE IF NOT EXISTS value_definition (id INTEGER PRIMARY KEY AUTOINCREMENT, metric_id TEXT NOT NULL, label TEXT NOT NULL, type TEXT NOT NULL, UNIQUE (metric_id, label), FOREIGN KEY (metric_id) REFERENCES metric (id) ON DELETE CASCADE) ''')
    conn.commit()
    conn.close()

# The following function inserts values into the metric table 
def insertValuesInMetric(code,desc):
    conn = sqlite3.connect(conf['dbName'])
    c = conn.cursor()
    try:
        c.execute("INSERT INTO metric (code, description) VALUES (?,?)",(code,desc))
    except:
        print("Skipped a duplicate entry")
    conn.commit()
    conn.close()

# The following function inserts values into the value_definition function
def insertValuesInValueDef(metric_id,label,type):
    conn = sqlite3.connect(conf['dbName'])
    c = conn.cursor()
    try:
        c.execute("INSERT INTO value_definition (metric_id, label, type) VALUES (?,?,?)",(metric_id,label,type))
    except:
        print("Skipped a duplicate entry")
    conn.commit()
    conn.close()

# The following function retrieves the id from metric table based on code
def getMetricId(code):
    conn = sqlite3.connect(conf['dbName'])
    c = conn.cursor()
    c.execute("SELECT id FROM metric WHERE code=?",(code,))
    id = c.fetchall()
    conn.commit()
    conn.close()
    return id[0][0]

# The following function reads the data from the csv and iterated through each row to populate the data in sql
def CSVtoSQL():
    df = pd.read_csv(conf['csvName'])
    metric_table = df[["metric_code","metric_description"]]
    metric_table.drop_duplicates(inplace=True)
    for index, row in metric_table.iterrows():
        insertValuesInMetric(row['metric_code'],row['metric_description'])
    
    value_table = df[["metric_code","value_label","value_type"]]
    for index, row in value_table.iterrows():
        id = getMetricId(row['metric_code'])
        insertValuesInValueDef(id,row['value_label'],row['value_type'])

#The following function is used by the front-end to retireve the values from the database metric table
def getMetricTable():
    conn = sqlite3.connect(conf['dbName']) 
    c = conn.cursor()
    c.execute("SELECT * FROM metric")
    details = c.fetchall()
    conn.commit()
    conn.close()
    d= []
    for detail in details:
        temp = {}
        temp['id'] = detail[0]
        temp['code'] = detail[1]
        temp['description'] = detail[2]
        d.append(temp)
    return d

#The following function is used by the front-end to retireve the values from the database value_definition table
def getValueDefinitionTable():
    conn = sqlite3.connect(conf['dbName'])
    c = conn.cursor()
    c.execute("SELECT * FROM value_definition")
    details = c.fetchall()
    conn.commit()
    conn.close()
    d= []
    for detail in details:
        temp = {}
        temp['id'] = detail[0]
        temp['metric_code'] = detail[1]
        temp['label'] = detail[2]
        temp['type'] = detail[3]
        d.append(temp)
    return d

def deleteDatabase():
    os.remove(conf['dbName'])
    return {"File deleted":True}

createTables()