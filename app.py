from flask import Flask, render_template,request
import numpy as numpy
import pymssql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        first_name = request.form.get("name")
        print(first_name)
        if first_name is not None:
            q1 = "SELECT * FROM [dbo].[test] WHERE Person = '" + first_name + "'"
        else:
            print("Empty value")
        conn = pymssql.connect(server='serveradb.database.windows.net', user='admin1', password='Ajithsivadas#1', database='assignment1')
        cursor = conn.cursor()
        cursor.execute(q1)
        result=cursor.fetchall()
        print(result[0][2])
        return render_template('search.html', picture=result[0][2],year=result[0][1])

    

