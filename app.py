from flask import Flask, render_template,request
import numpy as numpy
import pymssql
app = Flask(__name__)

@app.route('/')
def index():
    array1=[]
    conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1@serveradb', password='Ajithsivadas#1', database='assignment1')
    cursor = conn.cursor()
    q1="select * from [dbo].[people]" 
    cursor.execute(q1)
    result=cursor.fetchall()
    for i in result:
        j=numpy.asarray(i)
        array1.append(j)
    return render_template('main.html',result=array1)

@app.route('/search', methods=['POST', 'GET'])
def search_users():
    # if request.method == 'POST':
    #     first_name = request.form.get("name")
    #     print(first_name)
    #     if first_name is not None:
    #         q1 = "SELECT * FROM [dbo].[people] WHERE NAME = '" + first_name + "'"
    #     else:
    #         print("Empty value")
    #     conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1@serveradb', password='Ajithsivadas#1', database='assignment1')
    #     cursor = conn.cursor()
    #     cursor.execute(q1)
    #     result=cursor.fetchall()
    #     print(result[0][6])
        return render_template('search_user.html', user='chuck.jpg')

    

