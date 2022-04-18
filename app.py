#MOHANA PRABHA PALANISAMY
#1001886353
#CSE 6331 - Assignment 06


from flask import Flask, render_template,request, redirect, url_for
import numpy as numpy
import pymssql
import time
import redis
import hashlib
import pickle
from random import randint
from flask_socketio import SocketIO, emit,send

app = Flask(__name__)
socketio = SocketIO(app)
# myHostname = "redisadb.redis.cache.windows.net"
# myPassword = "CqXYuyQdw3MScVFMT3fkLyB4eAp9Zm0hOAzCaEc2SVE="
# r = redis.StrictRedis(host=myHostname, port=6380, password=myPassword, ssl=True)
server = 'adbassignment4.database.windows.net'
database = 'adb4'
username = 'admin1'
password = 'Ajithsivadas#1'   
conn = pymssql.connect(server=server, user=username, password=password, database=database)
cursor = conn.cursor()
playerName=""
gameRoom=0
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/playerdetails',methods=['POST','GET'])
def playerdetails():
   
    return render_template('player.html')

@app.route('/judgepage',methods=['POST','GET'])
def judgepage():
    return render_template('judge.html')

@app.route('/gameroom', methods=['POST','GET'])
def gameroom():
    playerName=request.form['player']
    cursor.execute("SELECT roomCode FROM assignment6 where isFull = 0")
    rows = cursor.fetchall()
    role=None
    print(rows)
    if len(rows) == 0:
        roomCode = randint(1,7000000)
        cursor.execute("SELECT roomCode FROM assignment6")
        rows1 = cursor.fetchall()
        while roomCode in rows1:
            roomCode = randint(1,7000000)
        cursor.execute("INSERT INTO assignment6 (roomCode,player1,isFull) VALUES ('"+str(roomCode)+"','"+str(playerName)+"','"+str(0)+"')")
        conn.commit()
        role = "player1"
       
        return render_template('lobby.html',playerName=playerName,roomCode=roomCode,role=role)
    else:
        roomCode = rows[0][0]
        print(roomCode)
        cursor.execute("SELECT player2 FROM assignment6 where roomCode = '"+str(roomCode)+"'")
        rows1 = cursor.fetchall()
        if rows1[0][0] is None:
            cursor.execute("UPDATE assignment6 SET player2 = '"+str(playerName)+"' WHERE roomCode = '"+str(roomCode)+"'") 
            conn.commit()
            role = "player2"
    global gameRoom
    gameRoom=roomCode
    return render_template('lobby.html',playerName=playerName,roomCode=roomCode,role=role)
        
@app.route('/judgedetails1', methods=['POST','GET'])
def judgedetails1():
    playerName=request.form['judgeName']
    print("UPDATE assignment6 SET judge = '"+str(playerName)+"', isfull='"+str(1)+"' WHERE roomCode = '"+str(gameRoom)+"'")
    print(gameRoom)
    cursor.execute("UPDATE assignment6 SET judge = '"+str(playerName)+"', isfull='"+str(1)+"' WHERE roomCode = '"+str(gameRoom)+"'")
    conn.commit()
    role = "admin"
    return render_template('judge_lobby.html',playerName=playerName,roomCode=gameRoom,role=role)

@app.route("/game/<roomCode>/<role>", methods=['POST','GET'])
def setGameSettings(roomCode,role):
   pile1 = request.form['pile1']
   pile2 = request.form['pile2']
   pile3 = request.form['pile3']
   min = request.form['min']
   max = request.form['max']
   firstPlayer = request.form['firstPlayer']
   print("UPDATE assignment6 SET pile1 = '"+str(pile1)+"', pile2 = '"+str(pile2)+"', pile3 = '"+str(pile3)+"', mini = '"+str(min)+"', maxi = '"+str(max)+"',firstPlayer = '"+str(firstPlayer)+"'  WHERE roomCode = '"+str(roomCode)+"'")
   cursor.execute("UPDATE assignment6 SET pile1 = '"+str(pile1)+"', pile2 = '"+str(pile2)+"', pile3 = '"+str(pile3)+"', mini = '"+str(min)+"', maxi = '"+str(max)+"',firstPlayer = '"+str(firstPlayer)+"'  WHERE roomCode = '"+str(roomCode)+"'")
   conn.commit() 
   cursor.execute("SELECT player1 FROM assignment6 where roomCode =  '"+str(gameRoom)+"'")
   rows = cursor.fetchall()
   player1 = rows[0][0]
   cursor.execute("SELECT player2 FROM assignment6 where roomCode =  '"+str(gameRoom)+"'")
   rows1 = cursor.fetchall()
   player2 = rows1[0][0]
   socketio.emit('start-game',{'roomCode':roomCode})
   return render_template('game_admin.html',roomCode=roomCode,pile1=pile1,pile2=pile2,pile3=pile3,min=min,max=max,player1=player1,player2=player2,role=role)

@app.route("/delcareWinner", methods=['POST','GET'])
def delcareWinner():
   roomCode = request.form['roomCode']
   winner= request.form['winner']
   player1 = request.form['player1']
   player2 = request.form['player2']

   cursor.execute("UPDATE assignment6 SET winner =  '"+str(winner)+"'WHERE roomCode = '"+str(roomCode)+"'")  
   conn.commit()
   if winner == "player1":
      name=player1
   else:
      name=player2
   return render_template('game_admin.html',roomCode=roomCode,name=name,gameOver=False)

@socketio.on('start-game')
def startGame(data):
   print("app.py startGame")
   roomCode = data['roomCode']
   role = data['role']
   socketio.emit("test",{'roomCode':roomCode,'role':role})
   return redirect(url_for('gamePlayer',roomCode=roomCode,role=role))   

@app.route("/gamePlayer/<roomCode>/<role>", methods=['POST','GET'])
def gamePlayer(roomCode,role):

   cursor.execute("SELECT * FROM assignment6 where roomCode =  '"+str(roomCode)+"'")  
   rows = cursor.fetchall()
   player1 = rows[0][1]
   player2 = rows[0][2]
   pile1 = rows[0][5]
   pile2 = rows[0][6]
   pile3 = rows[0][7]
   min = rows[0][8]
   max = rows[0][9]
   firstPlayer = rows[0][13]
   role=role
   return render_template('game_player.html',roomCode=roomCode,pile1=pile1,pile2=pile2,pile3=pile3,min=min,max=max,player1=player1,player2=player2,role=role,turn=firstPlayer)

@app.route("/gamePlayer/<roomCode>/<role>/removeStones", methods=['POST','GET'])
def removeStones(role,roomCode):
   # roomCode = request.form['roomCode']
   role = request.form['role']
   print(role)
   pile = int(request.form['pile'])
   stones = int(request.form['stones'])
   cursor.execute("SELECT * FROM assignment6 where roomCode =  '"+str(roomCode)+"'")
   rows = cursor.fetchall()
   pile1 = rows[0][5]
   pile2 = rows[0][6]
   pile3 = rows[0][7]
   min = rows[0][8]
   max = rows[0][9]
   player1 = rows[0][1]
   player2 = rows[0][2]

   if role=="player1":
      turn="player2"
   else:
      turn="player1"
  
   if pile == 1:
      newPile = pile1- stones
   elif pile == 2:
      newPile = pile2- stones
   elif pile == 3:
      newPile = pile3- stones
   print("newPile: "+str(newPile))
   if newPile>=0:
      cursor.execute("UPDATE assignment6 SET pile"+str(pile)+" =  '"+str(newPile)+"' WHERE roomCode = '"+str(roomCode)+"'")
      conn.commit()
      cursor.execute("SELECT * FROM assignment6 where roomCode = '"+str(roomCode)+"'")
      rows = cursor.fetchall()
      player1 = rows[0][1]
      player2 = rows[0][2]
      pile1 = rows[0][5]
      pile2 = rows[0][6]
      pile3 = rows[0][7]
      min = rows[0][8]
      max = rows[0][9]
      socketio.emit('update-pile',{'roomCode':roomCode,'turn':turn,'pile1':pile1,'pile2':pile2,'pile3':pile3,'pile':pile,'stones':stones})

      return render_template('game_player.html',roomCode=roomCode,pile1=pile1,pile2=pile2,pile3=pile3,min=min,max=max,player1=player1,player2=player2,role=role,turn=turn)
   else:
      pile1 = rows[0][5]
      pile2 = rows[0][6]
      pile3 = rows[0][7]
      return render_template('game_player.html',roomCode=roomCode,pile1=pile1,pile2=pile2,pile3=pile3,min=min,max=max,player1=player1,player2=player2,role=role,error="You can't remove more stones than you have",turn=role)

@app.route("/game/<roomCode>/declareWinner", methods=['POST','GET'])
def declareWinner(roomCode):
   winner = request.form['winner']
   cursor.execute("UPDATE assignment6 SET winner = ? WHERE roomCode = ?",(winner,roomCode))
   cursor.execute("SELECT * FROM assignment6 where roomCode = ?",(roomCode,))
   rows = cursor.fetchall()
   player1 = rows[0][1]
   player2 = rows[0][2]
   pile1 = rows[0][5]
   pile2 = rows[0][6]
   pile3 = rows[0][7]
   min = rows[0][8]
   max = rows[0][9]
   role = 'admin'
   socketio.emit('game-over',{'roomCode':roomCode,'winner':winner,'player1':player1,'player2':player2,'pile1':pile1,'pile2':pile2,'pile3':pile3})
   return render_template('game_admin.html',roomCode=roomCode,pile1=pile1,pile2=pile2,pile3=pile3,min=min,max=max,player1=player1,player2=player2,role=role,turn='player1',gameOver=True,winner=winner)
