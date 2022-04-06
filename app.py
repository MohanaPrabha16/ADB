from dataclasses import replace
from flask import Flask, render_template,request
import os.path
import nltk
import re
from nltk.stem.snowball import SnowballStemmer


app = Flask(__name__)
nltk.download('punkt')


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
def home():
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
   searchtext = request.form['searchtext']
   print(searchtext)
   searchTextList = searchtext.split(" ")
   for i in range(len(searchTextList)):
      searchTextList[i] =  stemmer.stem(searchTextList[i])
   lst=[]
   if searchtext.strip()!="":
      msg = "Search results for "+searchtext
      f = open("files/filelist.txt","r",errors='ignore')
      filelist = f.readlines()
      f.close()
      filelist = [x.strip() for x in filelist]
      for file in filelist:
         txt="./files/"+file
         with open(txt,"r",errors='ignore') as f:
            lines = f.readlines()
            for i in range(len(lines)):
               lines[i]=lines[i].strip()
               lines[i] = re.sub(r"http\S+", "", lines[i])
               lines[i] = re.sub(r'[^\w\,]+', ' ', lines[i])
               #lines[i]=re.sub('[^A-Za-z]+', ' ', lines[i])
               tokens = nltk.word_tokenize(lines[i])
               tokens=[x.lower() for x in tokens]
               stemmedWords = [stemmer.stem(x) for x in tokens]
               filteredWords=[]
               for word in stemmedWords:
                  if word not in englishStopWordsLoc and word not in spanishStopWordsLoc:
                     filteredWords.append(word)
               lines[i]=filteredWords

            with open("files/"+file, 'r',errors='ignore') as f1:
               origFile = f1.readlines()
            
            lst1=[]
            lineNum = []
            for x,line in enumerate(lines):
                  for i in line:
                     for j in searchTextList:
                        if i == j.lower() and x not in lineNum:
                           lineNum.append(x)
                           final = origFile[x]
                           final = final.replace("Â", "")
                           final = final.replace("â€™", "'")
                           final = final.replace("â€œ", '"')
                           final = final.replace('â€“', '-')
                           final = final.replace('â€', '"')
                           lst1.append(final.strip())
            if len(lst1)>0:
               lst.append([file,lst1])
      print(lst)
   else:
      msg="Please enter valid search text"
  
   return render_template('2.html',msg=msg,lst=lst)

   
if __name__ == '__main__':
    app.run()
    