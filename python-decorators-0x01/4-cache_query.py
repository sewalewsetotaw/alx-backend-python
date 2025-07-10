import time
import sqlite3 
import functools


query_cache = {}

"""your code goes here"""
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
def cache_query(func):
     @functools.wraps(func)
     def wrapper(conn,*args,**kwargs):
          if 'query' in kwargs:
               query=kwargs['query']
          elif args:
               query=args[0]
          else:
               query=None
          if query in query_cache:
               print("displaying query from catche")
               return query_cache[query]
          result=func(conn,*args,**kwargs)
          query_cache[query]=result
          print("[CACHE] Caching result for future use")
          return result
     return wrapper
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")