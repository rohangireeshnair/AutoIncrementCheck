from slackclient import SlackClient


######Enter the slack details here####

slack_token = 'xoxp-507960232848-508528273700-508594612211-47dc9dffb5906780c28bbfda7bf6510f'
channelname = 'mysql-autoincrement'
uname = 'autoincrementchecker'
workspaceURL = 'autoincrementchecker.slack.com'

####################

slack_client = SlackClient(token=slack_token)
def slackmsgsend(msg):
  ret=slack_client.api_call('chat.postMessage',
                          channel=channelname,
                          text=msg,
                          username=uname)
  if(ret['ok']):
    print('Alert posted on Slack channel {} in workspace {}'.format(channelname,workspaceURL))
  elif(ret['error']=='invalid_auth'):
    print('Authentication token is Invalid')
  elif(ret['error']=='missing_scope'):
    print("Permissions aren't given for the app in Slack. Please provide 'Post to specific channels in Slack' permission and retry")
