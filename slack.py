from slackclient import SlackClient


######Enter the slack details here####

slack_token = '' #Enter the slack authentication token with the quotes.
channelname = '' #Enter the slack authentication token with the quotes.
uname = ''  #Enter the username assigned to the app. For eg. if the permission mentioned in slack for the app is Send Message as incrementchecker then mention incrementchecker.
workspaceURL = ''#Enter the workspace URL.

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
