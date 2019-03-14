# coding:utf-8
import socket
import urllib.request
import urllib.error

# timeout 单位为秒
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('https://httpbin.org/post', data=data, timeout=30)
# print(response.read())


try:
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=3)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time Out')