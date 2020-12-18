import datetime; 
import mysql.connector;
import json;
from environment import host;


def timestamp():
    ct = datetime.datetime.now()
    return ct

def timediff(a,b):
    return(b-a)

def converter(d):
    return d.__str__()

def connection():

    a = timestamp()
    print(a)
    cnx = mysql.connector.connect(user='nivedha', password='nivedha',
                              host = host,
                              port=3306,
                              database='placement')
    mycursor = cnx.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM company")

    myresult = mycursor.fetchall()
    cnx.close()
    
    json_object = json.dumps(myresult,indent = 4 , sort_keys = True,default=converter)
    print(json_object)

    b = timestamp()
    print(b)
    print(timediff(a,b))

connection()


