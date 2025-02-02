import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection to MySQL
    mydb = mysql.connector.connect(
        host="localhost",  
        user="root",  
        password="C0operative"  
    )

    mycursor = mydb.cursor()

    # Create the database if it does not exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("Database connection closed.")
