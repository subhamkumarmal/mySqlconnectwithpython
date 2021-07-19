import mysql.connector
from mysql.connector import errors

def createConnection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="mysql",
            user="root",
            password="skm115",
            port="3306"
        )
    except(Exception, errors):
        print(errors)
    else:
        print("connections establihed")

    return conn

    #     return conn
    # except(Exception, Error) as error:
    #     print(error)