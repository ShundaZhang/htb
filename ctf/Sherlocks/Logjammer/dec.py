'''
https://github.com/jon-brandy/hackthebox/tree/main/Categories/Sherlocks/Logjammer

Logjammer
Write-up author: jon-brandy


Lesson learned:
Windows event log analysis.
Scenario:
You have been presented the opportunity to work as a junior DFIR consultant for a big consultancy, however they have provided a technical assessment for you to complete. The consultancy Forela-Security would like to gauge your knowledge on Windows Event Log Analysis. Please analyse and report back on the questions they have asked.

STEPS:
In this challenge we're given several windows event logs.
1ST QUESTION --> ANS: 27/03/2023 14:37:09


To identify the timestamp, we need to analyze the Security or Security_1 log.
Long story short, after sorted the timestamp from the oldest to newest, found a logon attempt with explicit credentials (eventID -> 4648) and cyberjunkie as it's username.

However, it does not explain whether the login attempt is succesfull or not. It can be successfully or it can't be.
But it concludes that this is the 1st attempt.
Hence let's convert the timestamp tp UTC using this online tool --> https://dateful.com/convert/utc.

2ND QUESTION --> ANS: Metasploit C2 Bypass


Analyzing the Windows Firewall-Firewall shall let us identify the name of the firewall rule added.

3RD QUESTION --> ANS: Outbound


The direction of the firewall rule is also stated there.

4TH QUESTION --> ANS: Other Object Access Events


Analyzing the Security_1 event log with eventID 4719, it states the subcategory of the changed policy.

5TH QUESTION --> ANS: HTB-AUTOMATION


To find the scheduled task created by cyberjunkie we just need to analyze the events with ID 4698 at Security_1 event log.

6TH QUESTION --> ANS: C:\Users\CyberJunkie\Desktop\Automation-HTB.ps1


Scrolling down at the exact ID shows the full path of the file.

7TH QUESTION --> ANS: -A cyberjunkie@hackthebox.eu


The argument is stated just below the file path.

8TH QUESTION --> ANS: SharpHound


To identify the tool, we need to analyze the Windows Defender-Operational event log.
Simply searching for eventID 1117 shows us the tool name.

9TH QUESTION --> ANS: C:\Users\CyberJunkie\Downloads\SharpHound-v1.1.0.zip


Scrolling down at the exact eventID's general tab, shows us the full path of the malware.

10TH QUESTION --> ANS: Quarantine


Scrolling down again at the exact eventID's general tab, you shall find the action taken by the antivirus.

11TH QUESTION --> ANS: Get-FileHash -Algorithm md5 .\Desktop\Automation-HTB.ps1


Analyzing Powerhell-Operational event log with 4104 as it's eventID, shows us the powershell command executed by the user.

12TH QUESTION --> ANS: Microsoft-Windows-Windows Firewall With Advanced Security/Firewall


This is a little bit tricky, took me a while to get the correct answer.
While analyzing the Security_1 event log, I noticed there is an event log which is cleared by cyberjunkie.

However if you tried to submit the event log cleared is --> Security, you shall get incorrect result.
After analyzing the Windows Firewall-Firewall event log, I found this eventID which explains this:

This should be our interest.
Submitting the log name shall gave you correct result.

IMPORTANT LINKS:
https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx
'''
