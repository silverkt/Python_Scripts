#!/usr/bin/env python3
# -*- coding: utf-8  -*- 

name = input("请输入您的姓名:");
print("亲爱的%s你好，您的年龄为%d" % (name,5),"岁");

for x in list(range(100)):
#	print(x);
        pass;
print('end');

a = '包含中文的输出';
 
print(a);

classmate = [
        'bob','silver','小米'
    ];

print(classmate[1]);

classmate = ('原则',2,'sss');

print(classmate[1]);

i = 0;
while i<10 :
        i+=1;
#        print(i);
else :
#        print('this is the end of story');
    pass;

for i in [30,45,50] :
#        print(i);
    pass;

i = list( i for i in range(20));
#print(i);
input();


# 模块相关
from datetime import datetime

now = datetime.now();
stamp = now.timestamp();

print(stamp);

import os

osname = os.name;
print(osname);


wget_es = {
    0: "No problems occurred.",
    2: "User interference.",
    1<<8: "Generic error code.",
    2<<8: "Parse error - for instance, when parsing command-line " \
        "optio.wgetrc or .netrc...",
    3<<8: "File I/O error.",
    4<<8: "Network failure.",
    5<<8: "SSL verification failure.",
    6<<8: "Username/password authentication failure.",
    7<<8: "Protocol errors.",
    8<<8: "Server issued an error response."
};

#print(wget_es);
import sys;


import requests,codecs

r = requests.get('http://www.sohu.com/');
#stra = 'a测试彩色试';
#print(stra);
print(type(r.text));

print(r.encoding);
r.encoding = 'gbk';

print(type(r.encoding));
#print(r.text);
#st = r.content;
#st = codecs.decode(st,oencoding='utf-8', errors='strict');
#st = st.encode('utf-8');
#st = r.text;
#print(st);

#f =codecs. open('d:/text.txt','wb','utf-8');
#f.write(st);
#f.close();

print(__name__);

url = 'http://sendcloud.sohu.com/webapi/mail.send.json';
data = {
        'api_user':'mymailsender_test_cevEkq',
        'api_key':'PJJUCyhMeBgOkxOO',
        'from':'itisagift@yeah.net',
        'fromname':'悦想城科技',
        'to':'1339964679@qq.com',
        'subject':'悦想城认证通知邮件',
        'html':'您的认证已通过，谢谢'
        }

data = {
        'api_user':'mymailsender_test_cevEkq',
        'api_key':'PJJUCyhMeBgOkxOO',
        'from':'itisagift@yeah.net',
        'fromname':'悦想城科技',
        'to':'1339964679@qq.com',
        'subject':'悦想城认证通知邮件',
        'html':'您的认证并未通过，请按要求更新您的资料后再次提交，谢谢'
        }

r = requests.post(url,data=data);

print(r.text);
