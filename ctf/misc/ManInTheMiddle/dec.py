#!/usr/bin/python3
#https://drive.google.com/file/d/1hgn5Z7khdKXZjg4hdHlX5MKiLYjCe6Ut/view
#https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2?permalink_comment_id=4339074#gistcomment-4339074

import json

k={
	"04":"A",
	"05":"B",
	"06":"C",
	"07":"D",
	"08":"E",
	"09":"F",
	"0a":"G",
	"0b":"H",
	"0c":"I",
	"0d":"J",
	"0e":"K",
	"0f":"L",
	"10":"M",
	"11":"N",
	"12":"O",
	"13":"P",
	"14":"Q",
	"15":"R",
	"16":"S",
	"17":"T",
	"18":"U",
	"19":"V",
	"1a":"W",
	"1b":"X",
	"1c":"Y",
	"1d":"Z",
	"1e":"1",
	"1f":"2",
	"20":"3",
	"21":"4",
	"22":"5",
	"23":"6",
	"24":"7",
	"25":"8",
	"26":"9",
	"27":"0",
	"2d":"_",
	"2f":"{",
	"30":"}"
}


fileData = open("data.json","r")
data=fileData.read()
JSONdata=json.loads(data)
for i in range (7,len(JSONdata)):
	c = JSONdata[i]["_source"]["layers"]["btl2cap"]
	if(c["btl2cap.length"]!="7"):
		try:
			lower=c["btl2cap.payload"][6:8]
			if(lower=="02"):
				print(k[c["btl2cap.payload"][12:14]],end="")
			else:
				print(k[c["btl2cap.payload"][12:14]].lower(),end="")

		except:
			print("",end="")
