# AutoIncrementCheck
A tool to check for overflowing columns in MySQL due to Auto Increment and if detected post an alert to Slack

Dependencies: Install the following python modules before running the script
  1.) slackclient
  2.) mysql-connector
  
  
 Before running the script Enter the slack workspace and channel information into slack.py file.
 
 The slack token is obtained by registering the app at https://api.slack.com/apps?new_app=1.
 On the slack app page the following permissions should be enabled.
  1.)chat:write:bot
  2.)incoming-webhook
  
  Note: In the chat:write:bot permission the heading will be mentioned as "Send message as xxxxxxxx". This xxxxxxxx is the       username that should be mentioned in the slack.py file.
 
 The script checks for Columns in database with autoincrement and those column's which have less than 10 rows left will be       reported as alert into the channel which is mentioned in slack.py file.
 
 Finally to Run the script Go to the folder where the script files are downloaded and type the following command.
    python3 init.py
    
 Note: The Script runs only on Python3.

