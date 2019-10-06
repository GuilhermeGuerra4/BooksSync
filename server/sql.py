import sqlite3

class DB:

	def __init__(self, dbname):
		self.dbname = dbname

	def conect(self):
		self.conn = sqlite3.connect(self.dbname)


	def query(self, query):

		try:
			self.conect()
			cur = self.conn.cursor()
			result = cur.execute(query)
			self.conn.commit()
			return result

		except sqlite3.Error as error: 
			print('ERRO: ', error)
		finally: 
			pass