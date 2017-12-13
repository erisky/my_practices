from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/tasks-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/tasks.readonly'
SCOPES = 'https://www.googleapis.com/auth/tasks'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Tasks API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'tasks-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Tasks API.

    Creates a Google Tasks API service object and outputs the first 10
    task lists.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('tasks', 'v1', http=http)

    tasks = service.tasks().list(tasklist='@default').execute()
    for task in tasks['items']:
        #print(task)
        if u'due' in task.keys():
            print (task['title'], task['due'])


#    task = {
#      'title': 'New Task',
#      'notes': 'Please complete me',
#      'due': '2010-10-15T12:00:00.000Z'
#    }

#    result = service.tasks().insert(tasklist='@default', body=task).execute()
#    print (result['id'])

#    results = service.tasklists().list(maxResults=10).execute()
#    items = results.get('items', [])
#    if not items:
#        print('No task lists found.')
#    else:
#        print('Task lists:')
#        print(items)
#        for item in items:
#            print(item[u'title'])
#            #print('{0} ({1})'.format(item[u'title'], item[u'id']))

if __name__ == '__main__':
    main()
