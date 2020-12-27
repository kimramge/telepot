# -*- coding: utf-8 -*-

from collections import deque

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton as BT
from telepot.namedtuple import InlineKeyboardMarkup as MU
from news_return import *
import time

token = '1476250644:AAEtz9YtAC88FNiY5AwWUKjdZEnUAGTVdjA'
#mc = '1269898121'

help_masege = "명령어를 받습니다.\n받고싶은 속보의 키워드를 정해주세요\nex)'전기차' '삼성' '코스피' 3가지의 속보를 받고싶다면\n@전기차@삼성@주가 <= 이렇게 입력해주세요"
bot = telepot.Bot(token)
loop = 0
btn_chek = 0

def btn_show(msg):
    btn1 = BT(text = "1. GO",callback_data = "1")
    btn2 = BT(text = "2. NO",callback_data = "2")
    mu = MU(inline_keyboard = [[btn1,btn2]])
    global MSG
    MSG = bot.sendMessage(msg['from']['id'], "go 누르면 시작한다(아무 메세지나 보내면 멈춤)",reply_markup=mu)
    global btn_chek
    btn_chek = 1



def query_ans(msg):
    query_data = msg["data"]
    if query_data == "1":
        bot.editMessageText(telepot.message_identifier(MSG), "시작")
        global loop
        loop = 1



    elif query_data =="2":
        bot.editMessageText(telepot.message_identifier(MSG),help_masege)
    global btn_chek
    btn_chek = 0

def handle(msg):
    global btn_chek
    if btn_chek == 1:
        bot.deleteMessage(telepot.message_identifier(MSG))
        btn_chek = 0
    print(msg)
    global mc
    mc = (msg['from']['id'])
    global loop
    loop = 0
    str1 = msg['text']
    str_list = []
    ntr_list = []
    real_list = []
    fact = 1
    print("입력받은 메세지 : ", str1)
    a = str1.find("@")
    b = str1.find("@")
    if a != -1:
        str_list.append(a)
        while str1[a + 1:].find('@') != -1:
            a = str1[a + 1:].find('@') + a + 1
            str_list.append(a)
            ntr_list.append(str1[b:a])
            b = a
        ntr_list.append(str1[a:len(str1)])
    for i in ntr_list:
        I = i[1:]
        I = str(I).strip()
        real_list.append(I)
        if len(str(i).replace(" ", "")) == 1: fact = 0

    print(real_list)
    if len(real_list) > 0 and fact == 1:
        bot.sendMessage(msg['from']['id'],"----키워드----")
        for i in real_list:
            bot.sendMessage(msg['from']['id'],'-' + i + '-')
        global keyword
        keyword = real_list
        btn_show(msg)

    else:
        bot.sendMessage(msg['from']['id'],"받고싶은 속보의 키워드를 정해주세요\nex)'코로나' '삼성' '코스피' 3가지의 속보를 받고싶다면\n@코로나@삼성@주가 <= 이렇게 입력해주세요")


MessageLoop(bot,{'chat' : handle,'callback_query' : query_ans}).run_as_thread()


while 1:
    time.sleep(1)
    link_list = deque(maxlen=60)
    chek_list = []
    while loop:
        time.sleep(3)
        test_list = []
        remak = mak(keyword)
        for i in remak:
            if i not in link_list:
                test_list.append(i)
                print(i, "를 test에 추가 하였습니다.")
            else:
                print(i, "는 이미 보냈음")
        for i in test_list:
            try:
                if loop == 1 :
                    bot.sendMessage(mc, text=i[1])
                    link_list.append(i)
                    time.sleep(3)
                else:break
            except Exception as e:
                print(e)
                print(type(e))
    pass

