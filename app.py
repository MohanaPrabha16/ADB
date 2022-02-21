from flask import Flask, render_template,request
import numpy as numpy
import pymssql
app = Flask(__name__)

@app.route('/')
def index():
    array1=[]
    q1='select * from [dbo].[earthquakes]'
    conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1', password='Ajithsivadas#1', database='assignment1')
    cursor = conn.cursor()
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)
    return render_template('main.html',result=array1)