from news_thebell import thebell
from news_naver import naver
kword = ["a","코","아","이","우"]


def mak(kword):
    news = []
    news_all = thebell() + naver()
    news_set = []

    for i in news_all:
        for j in range(0, len(kword)):
            if kword[j] in i[0]:
                news.append([i[0], i[1]])
                news_set.append(i[1])
                break
    if len(set(news_set)) == len(news) :print("같음")
    else : print("다름")

    return news

