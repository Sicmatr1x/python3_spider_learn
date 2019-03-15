# coding:utf-8
# 使用搭建在本地9743的代理
from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

# 可以添加多个代理
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'http://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https:www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)