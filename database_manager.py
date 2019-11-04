import MySQLdb

PASSWORD = "riflessipari"

db = None
cur = None

def start():
	global db
	global cursor
	db = MySQLdb.connect(host="localhost",
	                     user="admin",       
	                     passwd=PASSWORD, 
	                     db="pari")       

	cur = db.cursor()

def insert_user(gender, age):
	cur = db.cursor()
	QUERY = "INSERT INTO utente (`genere`, `eta`, `note`) VALUES ('{}', '{}', 'ok');".format(gender, age)
	cur.execute(QUERY)
	return cur

def commit():
	global db
	db.commit()

def close():
	global db
	db.close()

if __name__ == '__main__':
	start()
	insert_user("__test__", 23)
	commit()
	close()