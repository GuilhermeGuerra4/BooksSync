import os
import sqlite3
from config import Config

config = Config()
db = config.DBNAME


conn = sqlite3.connect(db)
cur = conn.cursor()

sql = """
	CREATE TABLE books(
		id integer PRIMARY KEY,
		name varchar(500) NOT NULL,
		filepath varchar(500) NOT NULL,
		imagepath varchar(500),
		readed boolean,
		data date NOT NULL
	)
"""

b = """INSERT INTO books (id, name, filepath, imagepath, readed, data) 
			VALUES (1, 'livro1', 'moises.pdf', 'wef', false, '2012-10-10')"""

a = """INSERT INTO books (id, name, filepath, imagepath, readed, data) 
			VALUES (2, 'livro2', 'maome.pdf', 'few', true, '2015-10-10')"""

cur.execute(a)
cur.execute(b)


conn.commit()