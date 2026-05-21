import sqlite3

#CONTANTS AND VARIABLES
DATABASE = 'books.db'

#FUNCTIONS


#MAIN CODE
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = 'SELECT * FROM books'
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
