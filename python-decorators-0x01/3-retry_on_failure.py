import time
import sqlite3 
import functools

#### paste your with_db_decorator here

""" your code goes here"""
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
         conn = sqlite3.connect('users.db')
         try:
                result=func(conn,*args,**kwargs)
                return result
         finally:
            conn.close()
    return wrapper
def retry_on_failure(retries,delay):
  def decorator(func):
     @functools.wraps(func)
     def wrapper(*args,**kwargs):
        for attempt in range(retries):
         try:
             result=func(*args,**kwargs)   
             return result
         except Exception as e:
             if attempt<retries-1:
                 print(f"[Retry {attempt + 1}/{retries}] Failed: {e}. Retrying in {delay}s...")
                 time.sleep(delay)
             else:
                 print(f"[FAILURE] All {retries} retries failed.")
                 raise
     return wrapper
  return decorator
@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users ")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)