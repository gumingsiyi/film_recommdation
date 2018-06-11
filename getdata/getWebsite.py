import urllib.request
import json
from bs4 import BeautifulSoup

import time


def getFeature(url):
    time.sleep(3)
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    referer = "https://movie.douban.com/tag/"
    #cookie = "Cookie:ll=\"118175\"; bid=ubTy8Pbdj_A; gr_user_id=433d5fed-aae1-4937-9098-b16389b9b954; __yadk_uid=OUdcW1rWSxWByR6WAXyCy96oDFhhCvYK; viewed=\"26154183_27178434_25982808_1981042\"; _vwo_uuid_v2=8FF5C782FFAE48B36198849BF20737D3|49137346aae3a1deb17c84637474ffbd; _ga=GA1.2.705908499.1498731099; ap=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.8464; __utmc=30149280; __utmz=30149280.1513848891.46.41.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utmz=223695111.1513848893.32.29.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ps=y; dbcl2=\"84643950:/OJodhzdF1g\"; ck=jRdE; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513855492%2C%22https%3A%2F%2Fwww.baidu.com%2F%3Ftn%3DSE_pshl0048_68avhk3a%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.705908499.1498731099.1513848891.1513855492.47; __utmb=30149280.0.10.1513855492; __utma=223695111.1296546438.1498784795.1513848893.1513855492.33; __utmb=223695111.0.10.1513855492; _pk_id.100001.4cf6=e70e180e2eb51565.1498784795.33.1513855631.1513849472."
    headers = {"User-Agent": user_agent, "Referer": referer}
    req = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html.read().decode('utf-8'), "lxml")
    temp = soup.find(name='div', attrs={"class": "tags-body"})
    array = temp.find_all(name='a')
    print(temp)
    res = []
    for i in array:
        print(i.string)
        res.append(i.string)
    print(res)
    return res


def getMovies(start):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    referer = "https://movie.douban.com/tag/"
    #cookie = "Cookie:ll=\"118175\"; bid=ubTy8Pbdj_A; gr_user_id=433d5fed-aae1-4937-9098-b16389b9b954; __yadk_uid=OUdcW1rWSxWByR6WAXyCy96oDFhhCvYK; viewed=\"26154183_27178434_25982808_1981042\"; _vwo_uuid_v2=8FF5C782FFAE48B36198849BF20737D3|49137346aae3a1deb17c84637474ffbd; _ga=GA1.2.705908499.1498731099; ap=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.8464; __utmc=30149280; __utmz=30149280.1513848891.46.41.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utmz=223695111.1513848893.32.29.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ps=y; dbcl2=\"84643950:/OJodhzdF1g\"; ck=jRdE; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513855492%2C%22https%3A%2F%2Fwww.baidu.com%2F%3Ftn%3DSE_pshl0048_68avhk3a%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.705908499.1498731099.1513848891.1513855492.47; __utmb=30149280.0.10.1513855492; __utma=223695111.1296546438.1498784795.1513848893.1513855492.33; __utmb=223695111.0.10.1513855492; _pk_id.100001.4cf6=e70e180e2eb51565.1498784795.33.1513855631.1513849472."
    headers = {"User-Agent": user_agent, "Referer": referer}
    req = urllib.request.Request(url="https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start="
                                     + start, headers=headers)
    html = urllib.request.urlopen(req)
    hjson = json.loads(html.read())
    data = hjson['data']
    # 数组长度
    for e in data:
        url = e['url']
        feature = getFeature(url)
        e['feature'] = feature
    return data
