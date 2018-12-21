diction = {'tinyint':127, 'tinyint unsigned':255, 'smallint':32767, 'smallint unsigned':65535,
           'mediumint':8388607, 'mediumint unsigned':16777215, 'int':2147483647, 'int unsigned':4294967295,
           'bigint':2**63-1, 'bigint unsigned':2**64-1}


def checkoverflowval(arr, dbvar):
    msg = "The tables that are about to run out of ID's are(less than 10 rows left): \n"
    flag = 0
    dbcursor = dbvar.cursor(buffered=True)
    for x in arr:
        dbcursor.execute("select max({}) from {}".format(x[1], x[0]))
        list = dbcursor.fetchall()
        item = list[0][0]
        if (str(item) == 'None'):
            item = 0
        item1=str(x[2]).split('(')[0]

        if(len(str(x[2]).split(' '))==2):
            item2=str(x[2]).split(' ')[1]
            final=item1+' '+item2;
        else:
            final=item1
        if(diction[final]-int(str(item))<10):
            flag=1
            msg=msg+'Table - {}\nColumn - {}\n\n\n'.format(x[0],x[1])
    if(flag==1):
        return msg
    else:
        return -1




