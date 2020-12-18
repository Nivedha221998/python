import datetime; 
import mysql.connector;
from environment import host;


def timestamp():
    ct = datetime.datetime.now()
    return ct

def timediff(a,b):
    return(b-a)

def connection():

    a = timestamp()
    print(a)
    cnx = mysql.connector.connect(user='nivedha', password='nivedha',
                              host = host,
                              port=3306,
                              database='placement')
    mycursor = cnx.cursor()
    mycursor.execute("SELECT * FROM placements")

    myresult = mycursor.fetchall()
    cnx.close()
    for x in myresult:
        print(x)

    b = timestamp()
    print(b)
    print(timediff(a,b))

connection()


