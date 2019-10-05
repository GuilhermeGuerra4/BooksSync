import os
from flask import Flask, request, render_template, url_for, redirect

App = Flask(__name__)

@App.route('/get', methods=['POST', 'GET'])
def Index():

	if 'teste' in request.files:
		teste = request.files['teste']
		if teste.filename != '':
			teste.save(os.path.join("C:/Users/guilherme/Desktop/booksSync/booksSync/server/uploads/",teste.filename))
			return 'ok'
		else:
			return 'nop'
	else:
		return 'bad request'	


if __name__ == "__main__":
	App.run(debug=True)

