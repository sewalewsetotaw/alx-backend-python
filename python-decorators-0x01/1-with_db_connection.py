import sqlite3 
import functools

def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
         conn = sqlite3.connect('users.db')
         try:
                result=func(conn,*args,**kwargs)
                return result
         finally:
            conn.close()
    return wrapper
@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) 
    return cursor.fetchone() 
    #### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id='00a6e072-4108-4c3b-8d2c-dc6e22b6a3e4')
print(user)