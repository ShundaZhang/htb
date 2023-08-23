'''
sudo apt install registry-tools

regshell -F query
\> ls
K AppEvents
K Console
K Control Panel
K Environment
K EUDC
K Keyboard Layout
K Network
K Printers
K Software
K System
\> cd Software
New path is: \Software
\Software> ls
K AppDataLow
K Google
K Microsoft
K Policies
K RegisteredApplications
K VMware, Inc.
K Wow6432Node
\Software> cd Microsoft
New path is: \Software\Microsoft
\Software\Microsoft> ls
K Active Setup
K Advanced INF Setup
K Assistance
K AuthCookies
K Avalon.Graphics
K CommsAPHost
K CTF
K EventSystem
K F12
K Feeds
K FTP
K IdentityCRL
K IME
K Input
K InputMethod
K InputPersonalization
K Internet Connection Wizard
K Internet Explorer
K Keyboard
K MediaPlayer
K MobilePC
K MSF
K Multimedia
K Narrator
K Osk
K Personalization
K Phone
K ScreenMagnifier
K Sensors
K ServerManager
K Speech
K Speech Virtual
K Speech_OneCore
K SystemCertificates
K TabletTip
K UEV
K WAB
K WcmSvc
K Windows
K Windows NT
K Wisp
\Software\Microsoft> cd CTF
New path is: \Software\Microsoft\CTF
\Software\Microsoft\CTF> ls
K Assemblies
K CUAS
K DirectSwitchHotkeys
K HiddenDummyLayouts
K SortOrder
K TIP
\Software\Microsoft\CTF> cd ..
New path is: \Software\Microsoft
\Software\Microsoft> ls
K Active Setup
K Advanced INF Setup
K Assistance
K AuthCookies
K Avalon.Graphics
K CommsAPHost
K CTF
K EventSystem
K F12
K Feeds
K FTP
K IdentityCRL
K IME
K Input
K InputMethod
K InputPersonalization
K Internet Connection Wizard
K Internet Explorer
K Keyboard
K MediaPlayer
K MobilePC
K MSF
K Multimedia
K Narrator
K Osk
K Personalization
K Phone
K ScreenMagnifier
K Sensors
K ServerManager
K Speech
K Speech Virtual
K Speech_OneCore
K SystemCertificates
K TabletTip
K UEV
K WAB
K WcmSvc
K Windows
K Windows NT
K Wisp
\Software\Microsoft> cd Win
Windows     Windows NT
\Software\Microsoft> cd Win
Windows     Windows NT
\Software\Microsoft> cd Windows
New path is: \Software\Microsoft\Windows
\Software\Microsoft\Windows> cd CurrentVersion
New path is: \Software\Microsoft\Windows\CurrentVersion
\Software\Microsoft\Windows\CurrentVersion> cd Run
New path is: \Software\Microsoft\Windows\CurrentVersion\Run
\Software\Microsoft\Windows\CurrentVersion\Run> ls
V "Windows Update" REG_SZ C:\Windows\System32\SFRCezFfQzRuX2t3M3J5XzRMUjE5aDd9.exe

echo SFRCezFfQzRuX2t3M3J5XzRMUjE5aDd9|base64 -d
HTB{1_C4n_kw3ry_4LR19h7}
'''
