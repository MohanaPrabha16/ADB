from flask import Flask, render_template,request
import numpy as numpy
import pymssql
app = Flask(__name__)

@app.route('/')
def index():
    array1=[]
    q1='select top 5 * from [dbo].[q2] order by mag desc'
    conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1', password='Ajithsivadas#1', database='assignment1')
    cursor = conn.cursor()
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)
    return render_template('main.html',result=array1)

@app.route('/1',methods=['POST','GET'])
def distance():
    array1=[]
    if request.method == 'POST':
        latitude= float(request.form.get('latitude'))
        N= float(request.form.get('degree'))

        list_of_data= []

        q1= "select * FROM [dbo].[q2] where (latitude'"+str(latitude)+"' and N '"+str(degree)+"') "
        conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1', password='Ajithsivadas#1', database='assignment1')
        cursor = conn.cursor()
        cursor.execute(q1)
        result=cursor.fetchall()
        for i in result:
            j=numpy.asarray(i)
            array1.append(j)
    return render_template('1.html',result=array1)


@app.route('/2',methods=['POST','GET'])
def dist():
    array1=[]
    if request.method == 'POST':
        place= str(request.form.get('place'))
        mag= float(request.form.get('mag'))
        mag= float(request.form.get('mag'))
        list_of_data= []

        q1= "select * from [dbo].[q2] where place like '%"+str(place)+"%'AND mag BETWEEN '"+str(mag)+"' AND '"+str(mag)+"'"
        conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1', password='Ajithsivadas#1', database='assignment1')
        cursor = conn.cursor()
        cursor.execute(q1)
        result=cursor.fetchall()
        for i in result:
            j=numpy.asarray(i)
            array1.append(j)
    return render_template('2.html',result=array1)

