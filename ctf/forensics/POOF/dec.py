'''
nc 157.245.37.125 30385

+-------+-----------------------------------------------------+
| Title |                     Description                     |
+-------+-----------------------------------------------------+
|  POOF |          In my company, we are developing a         |
|       |        new python game for Halloween. I'm the       |
|       |         leader of this project; thus, I want        |
|       |           it to be unique. So I researched          |
|       |    the most cutting-edge python libraries for game  |
|       |      development until I stumbled upon a private    |
|       |      discord server. One member suggested I try     |
|       |      a new python library that provides enhanced    |
|       |  game development capabilities. I was excited about |
|       |          it until I tried it. Quite simply,         |
|       |      all my files are encrypted now. Thankfully     |
|       |          I manage to capture the memory and         |
|       |        the network traffic of my Linux server       |
|       |        during the incident. Can you analyze it      |
|       |            and help me recover my files?            |
|       |                                                     |
+-------+-----------------------------------------------------+

Which is the malicious URL that the ransomware was downloaded from? (for example: http://maliciousdomain/example/file.extension)
> http://files.pypi-install.com/packages/a5/61/caf3af6d893b5cb8eae9a90a3054f370a92130863450e3299d742c7a65329d94/pygaming-dev-13.37.tar.gz
[+] Correct!

What is the name of the malicious process? (for example: malicious)
> configure
[+] Correct!

Provide the md5sum of the ransomware file.
> c010fb1fdf8315bc442c334886804e00
[+] Correct!

Which programming language was used to develop the ransomware? (for example: nim)
> python
[+] Correct!

After decompiling the ransomware, what is the name of the function used for encryption? (for example: encryption)
> mv18jiVh6TJI9lzY
[+] Correct!

Decrypt the given file, and provide its md5sum.
> 3bc9f072f5a7ed4620f57e6aa8d7e1a1
[+] Correct!

[+] Here is the flag: HTB{Th1s_h4ll0w33n_w4s_r34lly_sp00ky}

'''

'''
Volatility Usage of Customized Kernel/OS

https://github.com/volatilityfoundation/profiles
Copy Linux profiles to volatility/plugins/overlays/linux

If need to build kernel:
https://github.com/volatilityfoundation/volatility/wiki/Linux#getting-symbols
Identify the correct OS and kernel
Use docker image or standard OS image and download the target kernel
Build the kernel and zip the symbol files following the instructions above

But we don't need, we have already had the profile zip. Just put it into volatility folder.

pwd
/home/szhan21/volatility/volatility
cp ~/ctf/htb/ctf/forensics/POOF/Ubuntu_4.15.0-184-generic_profile.zip plugins/overlays/linux/
python vol.py --info |grep Linux
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dump --profile=LinuxUbuntu_4_15_0-184-generic_profilex64
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dmp --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 pslist
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dmp --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 linux_pslist
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dmp --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 linux_aux
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dmp --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 linux_psaux
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dmp --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 linux_lsof
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dmp --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 linux_netstat
python vol.py -f ~/ctf/htb/ctf/forensics/POOF/mem.dmp --profile=LinuxUbuntu_4_15_0-184-generic_profilex64 linux_bash

'''

'''
Decompile python executable

mv ~/pyinstxtractor.py .
ls
vi pyinstxtractor.py
python3 pyinstxtractor.py configure
ls
cd configure_extracted/
ls
uncompyle6 configure.pyc
cd ..
ls
vi dec.py
python3 dec.py
ls
md5sum candy_dungeon.pdf
file candy_dungeon.pdf

'''

from Crypto.Cipher import AES

filename = 'candy_dungeon.pdf.boo'
data = open(filename, 'rb').read()
key = 'vN0nb7ZshjAWiCzv'
iv = b'ffTC776Wt59Qawe1'
cipher = AES.new(key.encode('utf-8'), AES.MODE_CFB, iv)
pt = cipher.decrypt(data)

with open('candy_dungeon.pdf', 'wb') as f:
	f.write(pt)
