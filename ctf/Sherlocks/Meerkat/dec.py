'''
https://github.com/jon-brandy/hackthebox/tree/main/Categories/Sherlocks/Meerkat

Meerkat
Lesson learned:
Identifying Credential Stuffing attacks.
Bonitasoft CVE.
Packet filtering and custom column value.
Write-up author: jon-brandy


SCENARIO:
As a fast growing startup, Forela have been utilising a business management platform. Unfortunately our documentation is scarce and our administrators aren't the most security aware. As our new security provider we'd like you to take a look at some PCAP and log data we have exported to confirm if we have (or have not) been compromised.

STEPS:
In this challenge we're given two files.

1ST QUESTION --> ANS : Bonitasoft.


To answer it, I started by analyzing the .pcap file.
Found out that there are several request with POST method to 172.31.6.44. The endpoint is /bonita/loginservice.

Searching for Bonita at the .json file, shall resulting to Bonitasoft. Great now we know the ans is Bonitasoft.

2ND QUESTION --> ANS: Credential Stuffing.


Continue analyzing the logs, noticed several response with status code 401 which indicates unauthorized access.
I tried to follow few of them and found several different creds used.


If you noticed, the mail which used as the username always ends with .forela.co.uk. This indicates a company email.
Remembering status code is 401 for both (actually more), it means the attacker is bruteforcing.
The passwords also seem to be specific (?) and few of them seem to be complicated.
This kind of attacks is called Credential Stuffing.
3RD QUESTION --> ANS: CVE-2022-25237.


Searching for keyword CVE at the .json file shall found the answer for this.

4TH QUESTION --> ANS: i18ntranslation


Reading the CVE documentation, shall found a statement that the attacker is appending ;i18ntranslation or /../i18ntranslation/ to the end of an URL.
5TH QUESTION --> ANS: 56


To get the answer, a filter command is needed for quick analyze.
Simply execute --> urlencoded-form.key == "username".

To see the username value, luckily wireshark allows us to do custom columns.
Hence we can create a custom column --> edit -> preferences -> columns, then set the column type to custom.

Next, to modify the column, right click at the column area then choose edit column and set the fields to --> urlencoded-form.value.

Noticed at the bottom right it states 118 data displayed.

Scrolling down the packets, noticed several packets which unnecesarry is included.

Hence let's add another filter which denied install.
Filter command --> urlencoded-form.key == "username" && !(http contains "install").

Now it shows 59 but there are still duplicated username.

Hence the answer is 59 - 3 --> 56.
6TH QUESTION --> ANS: seb.broom@forela.co.uk:g0vernm3nt


To answer this, we can filter the response which status code is below 300. Filter command --> http.response.code < 300.

After analyzing each log, seems only the packets with status code 204 which is a response of the login request. 204 indicates the server has successfully fulfilled the request and that there is no additional content to send in the response payload body.


7TH QUESTION --> ANS: pastes.io


To answer this, we can simply filter the packet using --> http.request.method.

8TH QUESTION --> ANS: 0dc54416c346584539aa985e9d69a98e


To get the hash, we need to export the objects of our previous packet.

Running file command it states that the exported objects is a JSON data.
Reading it shall found the endpoint of the script used by hacker, run wget shall download the script.

To get the md5checksum simply run md5sum.

9TH QUESTION --> ANS: dbb906628855a433d70025b6692c05e7


Accessing the pastes.io shall resulting to this:

Based from the bash script, we can identified that hffgra4unv contains the public key.

Simply wget it then get the md5sum.

10TH QUESTION --> ANS: /home/ubuntu/.ssh/authorized_keys


The answer is the destination of the public key.

11TH QUESTION --> ANS:


Searching ssh shall resulting to these:

The first one should be our interest.

It discussed the same method used by the attacker.
IMPORTANT LINKS:
https://nvd.nist.gov/vuln/detail/CVE-2022-25237
https://attack.mitre.org/techniques/T1110/004/
'''
