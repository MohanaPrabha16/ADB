from flask import Flask, render_template
import numpy as numpy
import pymssql
app = Flask(__name__)

@app.route('/')
def index():
    array1=[]
    conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1', password='Ajithsivadas#1', database='assignment1')
    cursor = conn.cursor()
    q1="select * from [dbo].[people]" 
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)

    return render_template('main.html',result=array1)

