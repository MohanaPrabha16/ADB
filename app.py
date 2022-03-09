#MOHANA PRABHA PALANISAMY
#1001886353
#CSE 6331 - Assignment 03


from flask import Flask, render_template,request
import numpy as numpy
import pymssql
import time
import redis
import hashlib
import pickle
app = Flask(__name__)

myHostname = "redisadb.redis.cache.windows.net"
myPassword = "CqXYuyQdw3MScVFMT3fkLyB4eAp9Zm0hOAzCaEc2SVE="
r = redis.StrictRedis(host=myHostname, port=6380, password=myPassword, ssl=True)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/1',methods=['POST','GET'])
def createTable1():
    start= time.time()
    tablename= str(request.args.get('tablename'))
    array1=[]
    q1= "CREATE TABLE {}(time nvarchar(50) NOT NULL,latitude float NOT NULL,longitude float NOT NULL,depth float,mag float,type nvarchar(50) NOT NULL,gap float,net nvarchar(50),id nvarchar(50),place nvarchar(100));".format(tablename)
    conn = pymssql.connect(server='adb1.database.windows.net', user='admin1', port='1433', password='Ajithsivadas#1', database='AssignmentADB1')
    cursor = conn.cursor()
    cursor.execute(q1)
    end= time.time()
    diff=end-start
    return render_template('main.html',result=diff)
#5
@app.route('/2',methods=['POST','get'])
def random():
    start=time.time()
    array1=[]
    idFrom=request.args.get('idFrom')
    idTo = request.args.get('idTo')
    rand= request.args.get('id')
    print(rand)
    q1= "select * from [dbo].[ni] where id between '"+str(idFrom)+"' and '"+str(idTo)+"' order by id Desc"
    conn = pymssql.connect(server='adb1.database.windows.net', user='admin1', port='1433', password='Ajithsivadas#1', database='AssignmentADB1')
    cursor = conn.cursor()
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)
    end=time.time()
    diff=end-start
    return render_template('1.html',result=array1,time=diff)


#6a
@app.route('/3',methods=['POST','get'])
def random1():
    start=time.time()
    array1=[]
    idFrom=request.args.get('idFrom')
    idTo = request.args.get('idTo')
    rand= request.args.get('id')
    print(rand)
    q1= "select n.id,n.name,d.pwd,d.code from [dbo].[ni] n inner join [dbo].[di] d on d.id = n.id where n.id between '"+str(idFrom)+"' and '"+str(idTo)+"' order by id Desc "
    conn = pymssql.connect(server='adb1.database.windows.net', user='admin1', port='1433', password='Ajithsivadas#1', database='AssignmentADB1')
    cursor = conn.cursor()
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)
    end=time.time()
    diff=end-start
    return render_template('1.html',result=array1,time=diff)

@app.route('/4',methods=['POST','GET'])
def c():
    start=time.time()
    array1=[]
    idFrom=request.args.get('idFrom')
    idTo = request.args.get('idTo')
    list_of_data= []

    q1= "select n.id,n.name,d.pwd,d.code from [dbo].[ni] n inner join [dbo].[di] d on d.id = n.id where n.id between '"+str(idFrom)+"' and '"+str(idTo)+"' order by id Desc "
    conn = pymssql.connect(server='adb1.database.windows.net', user='admin1', port='1433', password='Ajithsivadas#1', database='AssignmentADB1')
    cursor = conn.cursor()
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)
    end=time.time()
    diff=end-start
    return render_template('4.html',result=array1,time=diff)

@app.route('/5',methods=['POST','GET'])
def cd():
    start=time.time()
    array1=[]
    location= str(request.form['location1'])
    depth_from= float(request.form['depthFrom1'])
    depth_to= float(request.form['depthTo1'])
    list_of_data= []

    q1= "select * from [dbo].[earthquakes] where place like '%"+str(location)+"%'AND depth BETWEEN '"+str(depth_from)+"' AND '"+str(depth_to)+"'"
    conn = pymssql.connect(server='adb1.database.windows.net', user='admin1', port='1433', password='Ajithsivadas#1', database='AssignmentADB1')
    cursor = conn.cursor()
    key = hashlib.sha224(q1.encode('utf-8')).hexdigest()
    if (r.get(key)):
        print("redis cached ")
    else:
        cursor.execute(q1)
        array1 = cursor.fetchall()
        r.set(key, pickle.dumps(array1) )
        r.expire(key, 3600)
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)
    end=time.time()
    diff=end-start
    return render_template('4.html',result=array1,time=diff)
