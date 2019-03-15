# coding:utf-8
# 解析链接
from urllib.parse import urlparse
print('---------------\nurlparse:')

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result) # class 'urllib.parse.ParseResult'
print(result)
print(result.scheme, result[0], result.netloc, result[1], sep=', ')



from urllib.parse import urlunparse
print('---------------\nurlunparse:')

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment'] # 长度必须为6
print(urlunparse(data))



from urllib.parse import urlsplit
print('---------------\nurlsplit:')

result1 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result1)
print(result1.scheme, result1[0])



from urllib.parse import urlunsplit
print('---------------\nurlunsplit:')

data1 = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment'] # 长度必须为5
print(urlunsplit(data1))



from urllib.parse import urljoin
print('---------------\nurljoin:')

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'http://cuiqiangcai.com/FAQ.html'))



from urllib.parse import urlencode
print('---------------\nurlencode:')

params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)


from urllib.parse import parse_qs
print('---------------\nparse_qs:')

query = 'name=germey&age=22'
print(parse_qs(query)) # 转字典



from urllib.parse import parse_qsl
print('---------------\nparse_qsl:')

query = 'name=germey&age=22'
print(parse_qsl(query)) # 转元组



from urllib.parse import quote
print('---------------\nquote:')

keyword = '壁纸'
url = 'https://www.baidu.com?wd=' + quote(keyword)
print(url)



from urllib.parse import unquote
print('---------------\nunquote:')

print(unquote(url))