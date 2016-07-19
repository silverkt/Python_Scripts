#!/bin/env/python3
#  --coding = utf-8--

import requests
import json


##
def searchDomain(domain) :
    url = 'http://checkdomain.xinnet.com/domainCheck?searchRandom=4&prefix='+domain+'&suffix=.com'
    r = requests.get(url)
    json_str = r.text.lstrip('null(').rstrip(')')
    json_list = json.loads(json_str)
    domain_status = json_list[0]['result'][0]
    if domain_status['yes'] != [] :
        return True
    else :
        return False
#####


res = searchDomain('baidu')
print(res)

full_str = 'abcdefghijklmnopqrstuvwxyz1234567890-'
nof_domain = 3
for s in full_str :
    print(s)
