from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

import sqlite3

import csv

conn = sqlite3.connect('database.db')



with open('people.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)


