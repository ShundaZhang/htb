'''
strings exatlon_v1
upx -d exatlon_v1

in main():
exatlon(local_38);
bVar1 = std::operator==(local_38,
                            "1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784  1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856  784 1776 1760 528 528 2000 "
                           );

in exatlon():
std::__cxx11::to_string(local_48,(int)local_21 << 4);

'''

f = [1152,1344,1056,1968,1728,816,1648,784,1584,816,1728,1520,1840,1664,784,1632,1856,1520,1728,816,1632,1856,1520,784,1760,1840,1824,816,1584,1856,784,1776,1760,528,528,2000] 

flag = ''
for i in f:
	flag += chr(i>>4)
print flag
#HTB{l3g1c3l_sh1ft_l3ft_1nsr3ct1on!!}
