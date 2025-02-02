import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",  # Assuming the database is on localhost
        user="root",  # Replace with your MySQL username
        password="yourpassword"  # Replace with your password
    )

    # Create a cursor object
    mycursor = mydb.cursor()

    # Create the database 'alx_book_store'
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection if it was established
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("Database connection closed.")

