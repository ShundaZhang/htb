'''
https://jsom1.github.io/_challenges/phish

szhan21@szhan21-NUC:~$ nslookup secure-startup.com
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   secure-startup.com
Address: 34.102.136.180

szhan21@szhan21-NUC:~$ nslookup -type=txt secure-startup.com
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
secure-startup.com      text = "v=spf1 a mx ?all - HTB{RIP_SPF_Always_2nd"

Authoritative answers can be found from:

szhan21@szhan21-NUC:~$ nslookup -type=txt _dmarc.secure-startup.com
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
_dmarc.secure-startup.com       text = "v=DMARC1;p=none;_F1ddl3_2_DMARC}"

Authoritative answers can be found from:


HTB{RIP_SPF_Always_2nd_F1ddl3_2_DMARC}
'''

'''
-type=soa: lookup for an soa (start of authority) record. Gives info about the domain, the email address of the domain admin, …
-type=any: lookup for any record
-type=ns: lookup for an ns (name server) record
-type=nx: lookup for an mx (mail exchange) record
-type=txt: lookup for an txt record. Apparently, TXT records are useful for multiple types of records like DKIM, SPF, etc. DKIM (Domain Keys Identified Mail) is an authentication technique by email. It allows the receiver to verify that an email has been sent and authorized by the domain’s owner. This is done by adding a DKIM signature to the email. If the DKIM signature is valid, the email hasn’t been modified. SPF (Sender Policy Framework) is an email validation system to prevent spammers from sending messages with our domain’s name. Finally, DKIM and SPF are used to build the DMARC (Domain-based message authentication, reporting and conformance), an email authentication, policy and reporting protocol.
'''
