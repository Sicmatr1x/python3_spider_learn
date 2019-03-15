# coding:utf-8
# 访问网站并获取 Cookies
import http.cookiejar, urllib.request

filename = 'cookies.txt'

# 保存成 Mozilla型浏览器的 Cookies格式
cookie = http.cookiejar.MozillaCookieJar(filename)
# 保存成 LWP(libwww-perl)格式的 Cookies
# cookie = http.cookiejar.LWPCookieJar(filename)

# 从文件读取 cookies
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)

cookie.save(ignore_discard=True, ignore_expires=True)