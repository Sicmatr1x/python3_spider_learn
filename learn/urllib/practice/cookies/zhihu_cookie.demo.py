# coding:utf-8

import requests

cookies = '_zap=d9b32e45-dbb4-4cd4-a9f7-6559822c8bcb; _xsrf=77ea7ed3-30dc-42b9-aa8b-b34eaf377ea2; d_c0="ANBm1aGf7Q2PTuCYHpUcc8kzCXh6MKCqgkc=|1532064946"; l_n_c=1; n_c=1; __utmc=51854390; __gads=ID=e798aba8eca95b15:T=1541572775:S=ALNI_Mbv6SBzIROq1BDdx-MMVrMEDNRvLQ; tst=r; q_c1=401f2704fee4481cb9ee2ea60f3c14af|1550824325000|1532064946000; r_cap_id="MzU0ODA4NzM5NmRhNDk0YjgxMTIxNmI1N2FkNTQxM2U=|1550824324|9d273fb221482963ccdfa7c723feacfee5f1bc3a"; cap_id="ZmQ2ZmIyMTlhMjhjNDc2YzkwYjI2N2MyMzRiY2JkZTE=|1550824324|f9a6b8365dbd4abff452475d7f32900c883ffb35"; l_cap_id="NDMzNjkzNjNhZTU3NGUxMjgyYjEwZTUwYmIxMmRhODI=|1550824325|0967844f777d72cb522839483c26ad82b041f1d1"; __utmz=51854390.1552447326.5.5.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20150702=1^3=entry_date=20150702=1; __utma=51854390.449733754.1540947052.1552447326.1552616693.6; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330',
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)