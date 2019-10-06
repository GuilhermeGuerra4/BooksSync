import os
import random
from sql import DB
from config import Config
from datetime import datetime
from flask import Flask, render_template, jsonify, request, send_from_directory

App = Flask(__name__)
App.config['UPLOAD_FOLDER'] =  'uploads/'

config = Config()

db = DB(config.DBNAME)


@App.route('/')
def Index():
	return render_template



#API
@App.route('/api/v1/get-books', methods=['GET'])
def GetBooks():
	result = db.query("""SELECT * FROM books""")
	result = result.fetchall()
	return jsonify(result)


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

	return jsonify(response)

@App.route('/api/v1/delete-book', methods=['POST'])
def DeleteBook():

	response = {'error':'false', 'msg':'ok'}

	if 'id' in request.form:
		book_id = request.form['id']
		result = db.query("""DELETE FROM books WHERE id LIKE '{}'""".format(book_id))

	else:
		response['error'] = 'true'
		response['msg'] = 'id not sent'

	return jsonify(response)

@App.route('/uploads/<string:folder>/<string:filename>')
def Files(folder, filename):
	return send_from_directory(os.path.join(App.config['UPLOAD_FOLDER'],folder), filename)


if __name__ == "__main__":
	App.run(debug=True)




