'''
unzip misDIRection.zip
Archive:  misDIRection.zip
   creating: .secret/
   creating: .secret/S/
[misDIRection.zip] .secret/S/1 password:
 extracting: .secret/S/1
   creating: .secret/V/
 extracting: .secret/V/35
   creating: .secret/F/
 extracting: .secret/F/2
 extracting: .secret/F/19
 extracting: .secret/F/27
   creating: .secret/o/
   creating: .secret/H/
   creating: .secret/A/
   creating: .secret/f/
   creating: .secret/r/
   creating: .secret/m/
   creating: .secret/B/
 extracting: .secret/B/23
   creating: .secret/a/
   creating: .secret/O/
   creating: .secret/h/
   creating: .secret/t/
   creating: .secret/2/
 extracting: .secret/2/34
   creating: .secret/7/
   creating: .secret/R/
 extracting: .secret/R/7
 extracting: .secret/R/3
   creating: .secret/b/
   creating: .secret/z/
 extracting: .secret/z/18
   creating: .secret/j/
 extracting: .secret/j/10
 extracting: .secret/j/12
   creating: .secret/P/
   creating: .secret/y/
   creating: .secret/d/
 extracting: .secret/d/13
   creating: .secret/Y/
   creating: .secret/q/
   creating: .secret/c/
   creating: .secret/6/
   creating: .secret/8/
   creating: .secret/U/
 extracting: .secret/U/9
   creating: .secret/p/
 extracting: .secret/p/32
   creating: .secret/W/
   creating: .secret/N/
 extracting: .secret/N/25
 extracting: .secret/N/11
 extracting: .secret/N/31
 extracting: .secret/N/33
   creating: .secret/g/
   creating: .secret/n/
   creating: .secret/e/
 extracting: .secret/e/5
   creating: .secret/1/
 extracting: .secret/1/30
 extracting: .secret/1/22
   creating: .secret/s/
 extracting: .secret/s/24
   creating: .secret/i/
   creating: .secret/3/
   creating: .secret/I/
   creating: .secret/D/
 extracting: .secret/D/26
   creating: .secret/X/
 extracting: .secret/X/29
 extracting: .secret/X/21
 extracting: .secret/X/17
   creating: .secret/Z/
   creating: .secret/4/
   creating: .secret/k/
   creating: .secret/9/
 extracting: .secret/9/36
   creating: .secret/J/
 extracting: .secret/J/8
   creating: .secret/C/
 extracting: .secret/C/4
   creating: .secret/v/
   creating: .secret/M/
   creating: .secret/0/
 extracting: .secret/0/6
   creating: .secret/G/
   creating: .secret/E/
 extracting: .secret/E/14
   creating: .secret/Q/
   creating: .secret/K/
   creating: .secret/5/
 extracting: .secret/5/16
   creating: .secret/x/
 extracting: .secret/x/15
   creating: .secret/l/
   creating: .secret/u/
 extracting: .secret/u/20
 extracting: .secret/u/28
   creating: .secret/L/
   creating: .secret/T/
   creating: .secret/w/

'''

d = [('S',1),('V',35),('F',2),('F',19),('F',27),('B',23),('2',34),('R',7),('R',3),('z',18),('j',10),('j',12),('d',13),('U',9),('p',32),('N',25),('N',11),('N',31),('N',33),('e',5),('1',30),('1',22),('s',24),('D',26),('X',29),('X',21),('X',17),('9',36),('J',8),('C',4),('0',6),('E',14),('5',16),('x',15),('u',20),('u',28)]

f = ['']*36

for i in d:
	f[i[1]-1] = i[0]

print ''.join(f).decode('base64')
#HTB{DIR3ctLy_1n_Pl41n_Si7e}
