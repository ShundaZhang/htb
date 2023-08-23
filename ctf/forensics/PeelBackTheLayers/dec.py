'''
https://ctftime.org/writeup/31438

docker pull steammaintainer/gearrepairimage
docker images
sudo snap install dive
dive 47f41629f1cf
#(nop) COPY file:0b1afae23b8f468ed1b0570b72d4855f0a24f2a63388c5c077938dbfdeda945c in /usr/share/lib/librs.so
docker save 47f41629f1cf > gearrepair.tar
strings librs.so

HTB{1_r34lly_l1k3_st34mpunk_r0b0ts!!!}
'''
