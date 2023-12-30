'''
https://github.com/jon-brandy/hackthebox/tree/main/Categories/Sherlocks/Litter


Litter
Write-up author: jon-brandy


Lesson learned:
DNS tunneling.
SCENARIO:
Khalid has just logged onto a host that he and his team use as a testing host for many different purposes, it’s off their corporate network but has access to lots of resources in network. The host is used as a dumping ground for a lot of people at the company but it’s very useful, so no one has raised any issues. Little does Khalid know; the machine has been compromised and company information that should not have been on there has now been stolen – it’s up to you to figure out what has happened and what data has been taken.

STEPS:
In this challenge we're given a .pcap file.
WIRESHARK


1ST QUESTION --> ANS: DNS


Analyzing the packets, it is known that most of the hostname is a large number of hexadecimals.

This pattern is referring to DNS tunneling technique, hence we can conclude the malicious protocol is DNS.
2ND QUESTION --> ANS: 192.168.157.145


Based from the previous malicious traffic we found, we can conclude the suspected host is --> 192.168.157.145.
3RD QUESTION --> ANS: whoami


Following one of the UDP packet streams and decode it with cyberchef, shall let us find the first command the attackers sends to the client.


4TH QUESTION --> ANS: 0.07


To identify the version of DNS tunneling tool used, simply analyze the previous decoded hex.
Scrolling down, we shall find the version.

5TH QUESTION --> ANS: win_installer.exe


Based from the previous question, we can assume that the attacker accidentally left the dns tool not renamed.
Hence, I scrolling down again and searched for a renaming command and found this:

As you can see, the attacker tried to use ren command which is a shorthand of rename in windows command.
6TH QUESTION --> ANS: 0


The users cloud storage is at OneDrive, scrolling down the decoded packet stream shall found out that there is no files inside it.
Hence, we can conclude the attacker did not locate any file in the user cloud storage.

7TH QUESTION --> ANS: C:\users\test\documents\client data optimisation\user details.csv


Again, scrolling down the same decoded packet stream, shall found the full path of PII file which is stolen.
Actually I found few .csv file which is interesting but only one so far that the attacker attempted to read.

Scrolling down again, you shall find the attacker indeed have an interest in this file and attempted to download it.

8TH QUESTION --> ANS: 721


To identify how many PII records were stolen, I download the cyberchef results and count manually there.
Took me a very long time to analyze it, maybe there's an intended way to solve it.
However, found out the amount of PII stolen is 721.
IMPORTANT LINKS:
https://www.socinvestigation.com/how-dns-tunneling-works-detection-response/

'''
