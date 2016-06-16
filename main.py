from pprint import pprint
import requests
import json
import sys

def usage():
   print("Argument needed") 
   print("script image_name")

if len(sys.argv) <= 1:
    print 'arg len = ', len(sys.argv)
    usage()
    sys.exit(1)

image_name = sys.argv[1]

try:
    data = requests.get('https://registry.hub.docker.com/v2/repositories/library/' + image_name + '/tags/')
except requests.exceptions.ConnectionError, e:
    print "No connection"
    sys.exit(1)
except:
    print "wtf?!"
    sys.exit(1)

formatted_data = json.loads(data.content)


for item in formatted_data['results']:
    print("Tag Name: {0}".format(item['name']))
    print("Size: {0}".format(int(item['full_size'])))
    print(' ')

#pprint(tags)
