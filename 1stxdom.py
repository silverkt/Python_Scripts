#!/bin/env/python3
#  --coding = utf-8--

import requests
import json
import random
import time
import sys
from bs4 import BeautifulSoup

sys.setrecursionlimit(2147483647)

###### revise searchDomain for 1stchina
def searchDomain(domain) :
    url = 'http://idc.1stchina.com/style/info/domaincheckpub.asp?domain='+domain+'&button=&com=yes&net=yes&org=yes'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    d = soup.input
    if d == None:
        return False
    d = next(d.children)
    if d == domain+'.com' :
        return True
    else :
        return False
    return False

## create domain
def collapeDomain(times=0, full_str='', s_str='') :
    times = times - 1
    if times != 0 :
        for s in full_str :
            for i in collapeDomain(times, full_str, s_str+s):
                yield i
            
    else :
        for s in full_str :
            yield s_str+s
    return 

full_str = 'abcdefghijklmnopqrstuvwxyz1234567890-'
times = 3
for domain in collapeDomain(times, full_str):
    time.sleep(1)
    if searchDomain(domain) == False :
        print(domain)
        pass
    else :
        print('--'+domain)
        with open('domains.txt', 'a+') as f :
            f.write(domain)


