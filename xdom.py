#!/bin/env/python3
#  --coding = utf-8--

import requests
import json
import random
import time
import sys
sys.setrecursionlimit(2147483647)

##
def searchDomain(domain) :
    url = 'http://checkdomain.xinnet.com/domainCheck?searchRandom='+str(random.randint(0,9))+'&prefix='+domain+'&suffix=.com'
    r = requests.get(url)
    json_str = r.text.lstrip('null(').rstrip(')')
    json_list = json.loads(json_str)
    domain_status = json_list[0]['result'][0]
    if domain_status['yes'] != [] :
        return True
    else :
        return False
#####

##res = searchDomain('baidu')
##print(res)




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
        with open('domains.txt', 'a+') as f:
            f.write(domain)
        
        
