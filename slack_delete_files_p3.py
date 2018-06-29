import urllib
import urllib.request
import time
import json
import sys

token = ''

#Delete files older than this:
days = 20
ts_to = int(time.time()) - days * 24 * 60 * 60

def check_arg():
    global token
    if len(sys.argv) > 1:
        token = sys.argv[1]
    else:
        print ("please input token")
        sys.exit()

def list_files():
  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 10000,
  }
  uri = 'https://slack.com/api/files.list'
  response = urllib.request.urlopen(uri + '?' + urllib.parse.urlencode(params)).read()
  return json.loads(response)['files']

def delete_files(file_ids):
  count = 0
  num_files = len(file_ids)
  for file_id in file_ids:
    count = count + 1
    params = {
      'token': token
      ,'file': file_id
      }
    uri = 'https://slack.com/api/files.delete'
    response = urllib.request.urlopen(uri + '?' + urllib.parse.urlencode(params)).read()
    print (count, "of", num_files, "-", file_id, json.loads(response)['ok'])

check_arg()
print (token)
files = list_files()
#print str(files)[1:-1]
file_ids = [f['id'] for f in files]
delete_files(file_ids)
