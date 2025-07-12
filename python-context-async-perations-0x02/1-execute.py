import sqlite3
import os

class ExecuteQuery:
 def __init__(self,dbpath,query,age):
   self.dbpath=os.path.abspath(dbpath)
   self.query=query
   self.age=(age,)
 def __enter__(self):
    self.conn=sqlite3.connect(dbpath)
    cursor=self.conn.cursor()
    cursor.execute(self.query,self.age)
    return cursor
 def __exit__(self, exc_type, exc_value, exc_traceback):
    self.conn.commit()
    self.conn.close()
if __name__=="__main__":
  dbpath="E:/ALX ProDev Back-End/alx-backend-python/python-decorators-0x01/users.db"
  query="SELECT * FROM users WHERE age > ?"
  age=25
  with ExecuteQuery(dbpath,query,age) as cursor:
    for row in cursor:
      print(row)