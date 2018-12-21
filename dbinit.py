import mysql.connector



def initiate(uname,passwd,dbname):

    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = uname,
        passwd = passwd,
        database = dbname
        )
    except mysql.connector.Error as err:
        print('Error occurred - {}'.format(err))
        return -1
    return mydb