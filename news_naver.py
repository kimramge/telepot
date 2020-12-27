import requests
import re
from bs4 import BeautifulSoup
import time


def naver():
    news = []
    raw = requests.get("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001",
                       headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("div > ul > li > dl > dt > a")

    for i in articles:
        if "img" in str(i):
            pass
        else:
            link = i['href']
            title = (i.text).strip()
            news.append([title, link])
    return news

