# coding:utf-8
from urllib import request, error

try:
    response = request.urlopen('https://cuiqiangcai.com/index.htm')
except error.URLError as e:
    print(e.reason)