import os
import random
from waitress import serve
from sql import DB
from config import Config
from datetime import datetime
from flask import Flask, render_template, jsonify, request, send_from_directory, make_response

App = Flask(__name__)
App.config['UPLOAD_FOLDER'] =  App.root_path+'/uploads/'

config = Config()

db = DB(config.DBNAME)

@App.route('/read/<path:link>')
def Read(link):
	return render_template("read.html", link=link)

@App.route('/')
def Index():
	return render_template("index.html")


#API
@App.route('/api/v1/get-books', methods=['GET'])
def GetBooks():
	result = db.query("""SELECT * FROM books""")
	result = result.fetchall()
	result = make_response(jsonify(result))
	result.headers['Access-Control-Allow-Origin'] = '*'
	return result


@App.route('/api/v1/add-book', methods=['POST'])
def AddBook():
	response = {'error':'false', 'msg':'ok'};

	if 'pdf' in request.files and 'img' in request.files:
		if 'title' in request.form:
			title = request.form['title']
			pdf = request.files['pdf']
			img = request.files['img']

			now = datetime.now()
			data = '{}-{}-{}'.format(now.year,now.month,now.day)

			pdfpath = os.path.join('uploads/pdf/', data+str(random.randint(1,100))+pdf.filename)
			imgpath = os.path.join('uploads/imgs/', data+str(random.randint(1,100))+img.filename)
			pdf.save(pdfpath)
			img.save(imgpath)

			db.query("""INSERT INTO books (id,name,filepath,imagepath,readed,data) 
				VALUES (NULL, '{}', '{}', '{}', '{}', '{}')""".format(title, request.host_url+pdfpath, request.host_url+imgpath, 'false', data))

		else:
			response['msg'] = 'title not sent'
	else:
		response['error'] = 'true'
		response['msg'] = 'files not sent'

	result = make_response(jsonify(response))
	result.headers['Access-Control-Allow-Origin'] = '*'
	return result

@App.route('/api/v1/delete-book', methods=['POST'])
def DeleteBook():

	response = {'error':'false', 'msg':'ok'}

	if 'id' in request.form:
		book_id = request.form['id']
		result = db.query("""DELETE FROM books WHERE id LIKE '{}'""".format(book_id))

	else:
		response['error'] = 'true'
		response['msg'] = 'id not sent'

	result = make_response(jsonify(response))
	result.headers['Access-Control-Allow-Origin'] = '*'
	return result

@App.route('/uploads/<string:folder>/<string:filename>')
def Files(folder, filename):
	return send_from_directory('C:/Users/guilherme/Desktop/booksSync/booksSync/server/uploads/{}'.format(folder), filename)


if __name__ == "__main__":
	serve(App, host='0.0.0.0', port=80)
	#App.run(host='0.0.0.0', port=5000)
	#App.run(debug=True)




