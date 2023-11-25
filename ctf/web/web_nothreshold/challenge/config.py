import os

class Config:
    DATABASE_URI = '/opt/www/app/nothreshold.db' 
    SECRET_KEY = os.urandom(69)
    FLAG = "HTB{f4k3_fl4g_f0r_t3st1ng}"
