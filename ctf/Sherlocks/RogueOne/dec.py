'''
https://github.com/jon-brandy/hackthebox/tree/main/Categories/Sherlocks/RogueOne

RogueOne
Write-up author: jon-brandy


Lessons Learned:
Using volatility3 to conduct memory forensics.
Identifying spoofed process by checking active connections and PPID for the active connections.
SCENARIO:
Your SIEM system generated multiple alerts in less than a minute, indicating potential C2 communication from Simon Stark's workstation. Despite Simon not noticing anything unusual, the IT team had him share screenshots of his task manager to check for any unusual processes. No suspicious processes were found, yet alerts about C2 communications persisted. The SOC manager then directed the immediate containment of the workstation and a memory dump for analysis. As a memory forensics expert, you are tasked with assisting the SOC team at Forela to investigate and resolve this urgent incident.

STEPS:
In this challenge we're given a memory dump which we can analyze using volatility.

1ST QUESTION --> ANS: 6812


Running a basic file check to identify what OS memory we're dealing with, shall resulting to windows.

Hence we can use windows plugin with volatility.
Looking for IOCs

Let's check for connections that are active at the time of the memory dump process.
Why looking for active connections?
-> Remembering the scenario said there is potential for C2 Communication from Simon Stark's workstation. Hence, it's easier for us to
identify the malicious process by checking active connections.
python3 ../../volatility3/vol.py -f 20230810.mem windows.netstat

Based from the results, the top 7 shall be our interest here. Because the rest mostly just being unestablished connections waiting for another user to connect.
Noticed one svchost.exe process standing out as communicate with uncommon port.

At this point, it's quite clear that the malicious PID is --> 6812 but to support our arguments, we can try to check parent process and child process for the top 7.
python3 ../../volatility3/vol.py -f 20230810.mem windows.pstree | grep -E '6136|8224|6812|8224|3404|8224|3404'

Great! 6812 indeed is the malicious PID, because cmd.exe comes out as the child process from the svchost.exe for the specified PID.
Not only that, we can identified another anomaly that the parent for the malicious svchost.exe is different than the other svchost.exe parent.

Checking for PID 7436 shall resulting to explorer.exe (File Explorer).

Nice! It is clear that PID 6812 is the malicious process.
How come svchost.exe becomes the malicious process?
--> As we know svchost.exe (Service Host) is a process used by windows to run or handle DLLs that the device needs to execute.
Knowing this, the attacker might spoof few legitimate processes, one of them is Service Host. 
2ND QUESTION --> ANS: 4364


Previously we already identified that the malicious PID spawned another process --> cmd.exe with PID 4364.
3RD QUESTION --> ANS: 5bd547c6f5bfc4858fe62c8867acfbb5


To identify the md5hash, we need to dump the process then execute md5sum for svchost.exe.img.
python3 ../../volatility3/vol.py -f 20230810.mem -o . windows.dumpfiles --pid 6812


4TH QUESTION --> ANS: 13.127.155.166:8888


Refering back to the previous result after executing netstat plugin, we can identified the C2 server's IP and PORT.

5TH QUESTION --> ANS: 10/08/2023 11:30:03


Again, we can identified the timestamp where the communication established using netstat plugin.

6TH QUESTION --> ANS: 0x9e8b87762080


This time to analyze the memory offset of the malicious process, we can view it by listing the process and filtering it only for the malicious PID using pslist or pstree.

7TH QUESTION --> ANS: 10/08/2023 11:58:10


To check when it submitted to virustotal, we just need to paste the md5sum at the search bar, then open the details tab and check the history section.

IMPORTANT LINKS
https://blog.onfvp.com/post/volatility-cheatsheet/
'''
