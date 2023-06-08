import string
import requests
import sys
import json

host = sys.argv[1]

url = 'http://'+host
response = requests.get(url)
print(response.text)


