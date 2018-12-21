import getpass
import dbinit
import dbcheck
import sys
import checkval
import slack



if __name__== "__main__":

        print("Welcome")
        dbvar=-1
        while(dbvar==-1):
            uname = input('Enter the mysql username')
            passwd = getpass.getpass(prompt="Enter the password")
            dbname = input('Enter the database name')
            dbvar = dbinit.initiate(uname,passwd,dbname)
            if(dbvar==-1):
                rep=input('Retry? (y/n)')
                if(rep=='y'):
                    continue
                else:
                    sys.exit(0)
        arr=dbcheck.checkdatabase(dbvar)
        msg=checkval.checkoverflowval(arr,dbvar)
        if(msg!=-1):
            slack.slackmsgsend(msg)
        elif(msg==-1):
            print("No tables with columns about to overflow")
            slack.slackmsgsend('No tables with columns about to overflow')



