from pony.orm import Database

db = Database(provider='sqlite', filename='sqldb.db',  create_db=True)
# db = Database(provider='postgres', user='username', password='password', host='localhost', database='dbname')
