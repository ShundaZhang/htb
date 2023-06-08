import requests
import sys
#import json
import hashlib

host = sys.argv[1]

url = 'http://'+host

rs = requests.session()
r = rs.get(url)
data = r.text.split('\n')[5].split('>')[3].split('<')[0]

md5 = hashlib.md5(data.encode()).hexdigest()
#headers = {'content-type': 'application/json'}
obj = {'hash': md5}

#r = rs.post(url, data=json.dumps(obj), headers=headers) #NOT work!
r = rs.post(url, data=obj)
print(r.text)
