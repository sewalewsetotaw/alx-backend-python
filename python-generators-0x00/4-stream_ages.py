import seed

def stream_user_ages():
    connection=seed.connect_to_prodev()
    if connection:
        cursor=connection.cursor()
        cursor.execute("SELECT age from user_data")
        for row in cursor:
            yield row[0]
        cursor.close()
        connection.close()

def calculate_average_age():   
    total=0
    count=0     
    for age in stream_user_ages():
        total+=age
        count+=1
    if count>0:   
        average=total/count
        print(f"Average age of users: {average:.2f}")
    else:
        print("no user found")

if __name__ == "__main__":
    calculate_average_age()