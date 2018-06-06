from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

import sqlite3
import csv


conn = sqlite3.connect('database.db')
# print("Opened database successfully")

# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print("Table created successfully")
# conn.close()


@app.route('/')
def home():
   return render_template('home2.html')


@app.route('/originals',methods = ['GET','POST'])
def originals():

      return render_template('originalspage.html')

@app.route('/duplicates',methods = ['GET','POST'])
def duplicates():

      return render_template('duplicatespage.html')


if __name__ == '__main__':
   app.run(debug = True)
