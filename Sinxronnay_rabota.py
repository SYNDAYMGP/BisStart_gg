
#(((--ОСНОВНОЙ КОД--TG)))

import pyautogui
from qe import main
ww2 = 'привет'
main(ww2)

#//////////////////////////////////
#//////////////////////////////////


#(((  БЛОК КОД DRF )))
def main(ww2):
    import time
    x = 5
    time.sleep(30)
    vv = x * ww2
    print(vv)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@










#(((--ОСНОВНОЙ КОД--TG)))


# В файле q1
from KOOD2 import main
model_engine = "gpt-3.5-turbo"


# Открываем файл для чтения
with open('1.txt', 'r', ) as file:
    # Инициализируем переменные
    current_variable = ""
    ww_vars = []
    # Читаем файл построчно
    for line in file:
        # Проверяем, содержит ли строка цифру
        if any(char.isdigit() for char in line):
            # Если переменная не пуста, сохраняем ее в список переменных
            if current_variable:
                ww_vars.append(current_variable)
            # Создаем новую переменную и добавляем текущую строку с цифрой
            current_variable = line
        else:
            # Добавляем текущую строку с текстом к текущей переменной
            current_variable += line
    # Добавляем последнюю переменную в список (если она не пуста)
    if current_variable:
        ww_vars.append(current_variable)
# Выводим результат
for i, variable in enumerate(ww_vars, 1):
    print(f"ww_vars[{i-1}]:\n{variable}")


text = "Принцип свободы совести и его реализация в различных сферах жизнедеятельности общества"
ll40 = main(ww_vars, text, model_engine)
print("=======================================================================================")
print(ll40)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import os
import re
import openai
import telebot
import time
import docx
from docx.shared import Pt
from docx import Document
import chardet




#(((  БЛОК КОД DRF )))
def main(ww_vars, text, model_engine):
    openai.api_key = "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"
    #####1гл   #####################################################
    #####1гл   #####################################################
    #####1гл   #####################################################
    ll4 = ""
    prompt = "расскажи по подробнее про (" + ww_vars[0] + ww_vars[1] + ww_vars[2] + ") , ответ должен быть расписан очень подробно и расказывать всю суть , по надобности приводить примеры того или иного, ответ дай в стиле реферата ,то есть ответ должен представлять чать реферата (" + text + ") "
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll4 = response['choices'][0]['message']['content']
    print(ll4)
    return ll4
    ##########################################################
    ##########################################################
    ##########################################################





