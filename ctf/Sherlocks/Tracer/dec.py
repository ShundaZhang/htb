'''
https://github.com/jon-brandy/hackthebox/tree/main/Categories/Sherlocks/Tracer

Tracer
Write-up author: jon-brandy


Lessons learned:
Analyzing windows event log file.
Parsing a prefetch file and extract the information into csv format using PECmd.
Parsing $MFT using MFTECmd.
Analyzing sysmon operational event log to identify fullname of the named Pipe ending with stderr.
SCENARIO:
A junior SOC analyst on duty has reported multiple alerts indicating the presence of PsExec on a workstation. They verified the alerts and escalated the alerts to tier II. As an Incident responder you triaged the endpoint for artefacts of interest. Now please answer the questions regarding this security event so you can report it to your incident manager.

STEPS:
In this challenge we're given few files of windows event log and prefetch files.

1ST QUESTION --> ANS: 9


To identify how many times was PsExec executed by the attacker, we need to analyze the Security event log file.
Analyzing the content of the latest log, we can identified the attacker's binary filename.

As you can see, it states Caller Process Name, it means the result is executed using this binary.
Hence, to check how many times it executed we just need to filter the Event ID displayed to --> 4625.

I count it manually, by reviewing each contents. Counted +1 if psexesvc.exe executed.
2ND QUESTION --> ANS: psexesvc.exe


Based from our previous identification, we identified the binary filename is --> psexesvc.exe.
3RD QUESTION --> ANS: 07/09/2023 12:06:54


Next, to get the timestamp for the 5th last instance of the PsExec, I tried to parse the prefetch file we extracted from the .zip file before.
Why prefetch file is the interest now?
-> Because Prefetch files is used to preloading certain data and code into memory.
Hence analyzing it helps us to understand the execution patterns of applications on a system,
as these files can provide insights into which applications are frequently used and how they are
loaded into memory during system startup.
To parse the prefetch file I used this online tool created by Eric Zimmerman.
.\PECmd.exe -f 'C:\Users\saput\Downloads\CYBERDEFENDER\Tracer\C\Windows\prefetch\PSEXESVC.EXE-AD70946C.pf'
RESULT



Noticed, there's a run count header which states 9. Another solution is to parse the prefetch file if we want to identify how many times a binary is executed.
Based from the Github's documentation, we can extract the information to a json or csv format.
I tried to extract the information into csv format and saved them to a directory named new_directory.
.\PECmd.exe -f 'C:\Users\saput\Downloads\CYBERDEFENDER\Tracer\C\Windows\prefetch\PSEXESVC.EXE-AD70946C.pf' --csv new_directory

The output_timeline csv should be our interest here.

Simply viewing the timeline for the 6th row shall gave us the correct timestamp.

4TH QUESTION --> ANS: FORELA-WKSTN001


To identify the hostname, we just need to view the Files Referenced result from the prefetch parser.

5TH QUESTION --> ANS: PSEXEC-FORELA-WKSTN001-95F03CFE.key


To identify the fullname of the key file dropped by 5th last instance, we can try to parse the Master File Table (MFT).
MFT stands for Master File Table, and it is a crucial component of the NTFS (New Technology File System) file system used in Windows operating systems.
The MFT is a database that stores information about every file and directory on an NTFS-formatted volume.
It acts as a centralized index, keeping track of metadata for each file, including attributes such as file name, size,
creation time, permissions, and the location of the file data on the disk.
To parse it, we can use an online tool created by Eric Zimmerman named MFTECmd.
I tried to extract the information into csv format and stored it on a directory named --> mftparse_result.
.\MFTECmd.exe -f 'C:\Users\saput\Downloads\CYBERDEFENDER\Tracer\C\$Extend\$J' --csv mftparse_result

Upon analyzing the csv file, I noticed the timestamp is descending. To get the correct key, we just need to search for timestamp which is ONE SECOND different than the execution of the last 5th instance.
Long story short, I managed to find the correct key at row 145570. Noticed the timestamp is different one second only.

Alternatives way to identify it, simply check the results from PECmd.exe at the Files Referenced header.

6TH QUESTION --> ANS: 07/09/2023 12:06:55


We managed to find the timestamp previously.
7TH QUESTION --> ANS: \PSEXESVC-FORELA-WKSTN001-3056-stderr


To identify the fullname of the named Pipe ending with stderr keyword, we can start by analysing Sysmon event log.

Sysmon logs events related to various system activities, providing detailed information about processes, network connections, file creation, registry modifications, and more. The information logged by Sysmon can be crucial for detecting and investigating security incidents.
As we know, sysmon provide many event log. However there is a way to speeding the analysis, first we just need to analyze the same timestamp as the 5th.
Then our second interest is this timestamp:

Just focusing when the second timestamp is close to 12:06:55.
Long story short, found the correct name.

IMPORTANT LINKS
https://github.com/EricZimmerman/PECmd
https://ericzimmerman.github.io/#!index.md
https://github.com/EricZimmerman/MFTECmd
'''
