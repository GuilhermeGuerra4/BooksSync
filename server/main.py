import os
from sql import DB
from config import Config
from flask import Flask, render_template, jsonify

App = Flask(__name__)

config = Config()

db = DB(config.DBNAME)


@App.route('/')
def Index():
	return render_template('index.html')


@App.route('/get-books', methods=['GET'])
def GetBooks():
	result = db.query("""SELECT * FROM books""")
	result = result.fetchall()
	return jsonify(result)


@App.route('/get-book/<int:id>', methods=['GET'])
def GetBook(id):
	return ''

@App.route('/add-book', methods=['POST'])
def AddBook():
	return ''

@App.route('/delete-book', methods=['POST'])
def DeleteBook():
	return ''



if __name__ == "__main__":
	App.run(debug=True)




