import requests
import re
from bs4 import BeautifulSoup
import time

def thebell():
    news = []
    raw = requests.get("https://www.thebell.co.kr/free/content/Article.asp?svccode=00",
                       headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"})
    html = BeautifulSoup(raw.text, "html.parser")


    #contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li:nth-child(1)

    articles = html.select("div > div > div > div > div > ul > li > dl > a")
    # contents = html.select("div > div > div > div > div > ul > li > dl > a > dd")

    for i in articles:
        #print('https://www.thebell.co.kr/free/content/'+i['href'],i['title'])
        news.append([i['title'],'https://www.thebell.co.kr/free/content/'+i['href']])
    return news
    # for i in contents:
    #     print(i.text)


