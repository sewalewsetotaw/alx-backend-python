import seed
#    Generator that yields batches of users from the database.
#    Each batch contains `batch_size` number of users.
def stream_users_in_batches(batch_size):
    connection=seed.connect_to_prodev()

    if connection:
        cursor=connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        batch=[]
        for row in cursor:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch=[]
        if batch:
            yield batch
        cursor.close()
        connection.close()
def batch_processing(batch_size):
    # Processes each batch to filter and print users over age 25.
   for batch in stream_users_in_batches(batch_size):
       for user in batch:
           if user['age']>25:
               print(user)
   return