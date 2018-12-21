import mysql

def checkdatabase(dbvar):
    dbcursor = dbvar.cursor(buffered=True)
    dbcursor.execute("show tables");
    tablelist=dbcursor.fetchall()
    autoinclist = []
    for x in tablelist:
        dbcursor.execute("select COLUMN_TYPE, COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{}' AND EXTRA like '%auto_increment%'".format(x[0]))
        list = dbcursor.fetchall()
        if(len(list)!=0):
            for y in list:
                datatype =str(y[0])
                datatype=datatype.split("'")[1]
                autoinclist.append((x[0],y[1],datatype))
    return autoinclist

