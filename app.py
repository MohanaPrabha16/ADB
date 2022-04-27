from dataclasses import replace
from flask import Flask, render_template,request
import os.path
import nltk
import re
from nltk.stem.snowball import SnowballStemmer
from nltk.probability import FreqDist
from collections import Counter

app = Flask(__name__)
nltk.download('punkt')

conn = pymssql.connect(server='adbassignment4.database.windows.net', user='admin', password='Ajithsivadas#1', database='adb4')
cursor = conn.cursor()

englishStopWordsLoc="./englishStopWords.txt"
spanishStopWordsLoc = "./spanishStopWords.txt"

with open(englishStopWordsLoc,'r') as f1:
    englishStopWords=f1.readlines()
    englishStopWords= [i.strip() for i in englishStopWordsLoc]

with open(spanishStopWordsLoc,'r') as f1:
    spanishStopWordsLoc=f1.readlines()
    spanishStopWordsLoc= [i.strip() for i in spanishStopWordsLoc]

stemmer = SnowballStemmer(language='english')

@app.route('/')
def main():
   print(1)
   return render_template('main.html')

@app.route('/1')
def addnew():
   return render_template('1.html')

@app.route('/2')
def search():
   return render_template('2.html')


@app.route('/1form',methods = ['POST', 'GET'])
def addnewfileform():
   filename = request.form['filename']
   filecontent = request.form['filecontent']
   msg=""
   if os.path.isfile("files/"+filename+".txt"):
      msg = "File "+filename+" already exists"
      return render_template('1.html',msg=msg)
   
   if(filename.strip()!="" and filecontent.strip()!=""):
      name="files/"+filename+".txt"
      fw =open(name,"w+")
      fw.write(filecontent)
      fw.close()
      f = open("files/filelist.txt", "a")
      f.write(filename+".txt\n")
      f.close()
      msg="File "+filename+" creation was successful"
   else:
      msg="Enter valid file name and file content"
   return render_template('1.html',msg=msg)


@app.route('/send',methods = ['POST', 'GET'])
def send():
   print(1)
   number1 = request.form['number1']
   number2 = request.form['number2']
   searchtext = request.form['searchtext']
   print(searchtext)
   split_it = searchtext.split()
   from collections import Counter
   Counter = Counter(split_it)
   most_occur = Counter.most_common(int(number1))
   
   return render_template('2.html',msg=most_occur)

   
if __name__ == '__main__':
    app.run()
    