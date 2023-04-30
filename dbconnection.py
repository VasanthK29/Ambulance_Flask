import mysql.connector as mysql

class dbDetection:
    connection = mysql.connect(
        host="localhost",
        user="root",
        password="",
        database="detection"
    )
