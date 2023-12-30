'''
https://github.com/jon-brandy/hackthebox/tree/main/Categories/Sherlocks/Bumblebee

Bumblebee
Write-up author: jon-brandy


Lesson learned:
Analyzing sqlite3 file.
SCENARIO:
An external contractor has accessed the internal forum here at Forela via the Guest WiFi and they appear to have stolen credentials for the administrative user! We have attached some logs from the forum and a full database dump in sqlite3 format to help you in your investigation.

STEPS:
In this challenge, we're given 2 files. A log file and a sqlite3 file.
1ST QUESTION --> ANS: apoole1


To get the username of the external contractor, we can start by accessing the sqlite3 database dump.
I start by execute query --> SELECT name FROM sqlite_master WHERE type='table';, which resulting to a few results. But one table_name caught should be our interest.

Execute this query --> SELECT * FROM phpbb_users; to check all columns and it's value.

Noticed, there's a username with contractor mail, hence we can identified the external contractor is should be apoole or apoole1.
2ND QUESTION --> ANS: 10.10.0.78


To identify the IP address, we need to just need to check the column value.

3RD QUESTION --> ANS: 9


To find the malicious post that the contractor made, we need to enumerate tables in the database and search for post_id column.
Long story short, I found one table that should be our interest, the phpbb_posts table.
Noticed at post_id 9, the poster_ip is the exact same as the contractor's ip.

Then, analyzing the post_text we can intrepret that the contractor post is indeed malicious.

I'm SPECULATING that the contractor tried to do XSS to get users's cookie.


4TH QUESTION --> ANS: http://10.10.0.78/update.php


For the URI path, we just need to analyze the malicious content.

Searching for the attacker's ip address shall gave us the URI path.

Why searching for the attcker's IP?
-> Since I am SPECULATING that the attacker is doing XSS to steal user's cookie, hence the attacker COULD be
reflected the cookie back him.
5TH QUESTION --> ANS: 26/04/2023 10:53:12


To find the UTC time, I started by analyzing the access.log file but did not find any supporting evidence.
Hence, I started to analyze the phpbb_log table and found a column named log_operation which indicates a successful login attempt for admin role.

RESULT


6TH QUESTION --> ANS: Passw0rd1


To get the password name, I just strings the database and grep for "ldap".
RESULT


7TH QUESTION --> ANS: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36


Simply check the user agent for ip --> 10.255.254.2 because we already identified before that the IP is Forela's.

8TH QUESTION --> ANS: 26/04/2023 10:53:51


Again, we need to check LOG OPERATION to get the time.

As you can see, after the attacker successfully logged in as admin, he began to add his own user account as part of the admin group.

To identify the timestamp, simply convert the epoch time to UTC.

9TH QUESTION --> ANS: 26/04/2023 11:01:38


This time, I found the evidence when reviewing the access.log file.

Previously at table phpbb_log we can identify that the attacker attempted to do DB backup, then the timestamp is added at the backup's filename.
At this point, we are VERY sure this is the backup file.
Based from this log's line, we can see a GET request is made, the attacker tried to download the backup file the system previously created.
To get the UTC timestamp, simply substract 12 by 1 because the log's timestamp is +1.
10TH QUESTION --> ANS: 34707


Besides the status code, we can see the bytes or lengths for current request.

IMPORTANT LINKS
https://sqliteviewer.app/
https://www.epochconverter.com/
'''
