# coding:utf-8
from urllib import request, error

try:
    response = request.urlopen('https://cuiqiangcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, seq='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')