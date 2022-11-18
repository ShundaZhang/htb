'''
https://medium.com/write-ups-hackthebox/c%C3%B3mo-resolver-monstrosity-c55be6194485
Need tweet consumer key and secret...

git clone https://github.com/x0rz/tweets_analyzer
python tweets_analyzer.py -n miounster --limit 3000 -s
python prettyJSON.py tweets/miounster/2018–01–10_17–12–13.json | grep -A 2 "coordinates \": \ \["| grep" \. "| sed 's /, // g' | sed 's / // g' | rs 0 2 | sed 's / /, /' > muestra.txt

https://www.gpsvisualizer.com/map_input?form=data

407180f14EBB5D998E0083034ED9A21B

https://crackstation.net/

HTB{covertops}

'''
#!/usr/bin/python3

import re

with open('twdump.txt', 'r') as f:
	lines = f.readlines()

for line in lines:
	m = re.match(r'.*\"coordinates\": \[(.*, .*)\].*"coordinates\": \[(.*, .*)\].*', line, re.M|re.I)
	if m:
		print(m.group(1))
		print(m.group(2))
