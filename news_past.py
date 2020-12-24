import re
from coin import *
from time import sleep
from collections import deque
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ChatAction
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler,CallbackQueryHandler


token = '1450738289:AAE2JHmPgEXCL_dfrTg2u71Zb86nZ9ynFZY'

updater = Updater(token=token)#, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="명령어를 받습니다.\n받고싶은 속보의 키워드를 정해주세요\nex)'전기차' '삼성' '코스피' 3가지의 속보를 받고싶다면\n@전기차@삼성@주가 <= 이렇게 입력해주세요")

def echo(update, context):
    str_list = []
    ntr_list = []
    real_list = []
    fact = 1
    # text = "너 지금 \'"+update.message.text+"\'이라 했니?"
    # context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    str1 = update.message.text
    print("입력받은 메세지 : ",str1)
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
        if len(str(i).replace(" ","")) == 1:fact=0



    print(real_list)
    if len(real_list) > 0 and fact == 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="----키워드----")
        for i in real_list:
            context.bot.send_message(chat_id=update.effective_chat.id, text='-'+i+'-')

        global keyword
        keyword = real_list

        task_buttons = [[
            InlineKeyboardButton('1.시작', callback_data=1)
            , InlineKeyboardButton('2.다시입력', callback_data=2)
        ]]

        reply_markup = InlineKeyboardMarkup(task_buttons)

        context.bot.send_message(
            chat_id=update.message.chat_id
            , text='작업을 선택해주세요.'
            , reply_markup=reply_markup
        )

    else: context.bot.send_message(chat_id=update.effective_chat.id, text="오류가 있습니다.\n다시 입력해 주세요.\n( 사용법은 /start 라고 입력하시면 나옵니다.)")

def cb_button(update, context):
    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )

    if data == '1':
        context.bot.edit_message_text(
            text='작업을 시작합니다.'.format(data)
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id

        )

        crawl_navernews(update, context)
    elif data == '2':
        context.bot.edit_message_text(
            text="명령어를 받습니다.\n받고싶은 속보의 키워드를 정해주세요\nex)'전기차' '삼성' '코스피' 3가지의 속보를 받고싶다면\n@전기차@삼성@주가 <= 이렇게 입력해주세요".format(data)
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )
        crawl_zigbang()



def crawl_navernews(update, context):
    print('뉴스 크롤링을 시작합니다.')
    link_list = deque(maxlen=40)
    chek_list = []

    while 1:
        time.sleep(3)
        test_list = []
        remak = mak(keyword)
        for i in remak:
            if i not in link_list:
                test_list.append(i)
                chek_list.append(i[1])
                print(i, "를 test에 추가 하였습니다.")
            else:
                print(i, "는 이미 보냈음")
        for i in test_list:
            try:
                context.bot.send_message(chat_id=update.effective_chat.id, text=i[1])
                link_list.append(i)
                time.sleep(3)
            except Exception as e:
                print(e)
                print(type(e))

        print(len(chek_list) - len(set(chek_list)))


def crawl_zigbang():
    pass



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

button_callback_handler = CallbackQueryHandler(cb_button)
dispatcher.add_handler(button_callback_handler)



updater.start_polling()
updater.idle()

