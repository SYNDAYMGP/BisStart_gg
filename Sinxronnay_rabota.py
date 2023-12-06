# Файл KOOD1.py
import KOOD2
KOOD2.main()
############################
###########################
##########################
###########################
############################
# Файл KOOD2.py
def main():
    import os
    import re
    import openai
    import telebot
    import time
    import docx
    from docx.shared import Pt
    from docx import Document
    import chardet

    openai.api_key = "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"
    model_engine = "gpt-3.5-turbo"
    text = 'Госдума в РФ'
    ll2 = ""
    prompt = "составь мне план (структуру) для моего доклада на тему (" + text + ") план должен состоять из шести глав ,а главы должны состоять из двух под глав, в ответ ты должен записать только название глав и название подглав к ним без каких либо твоих пояснений и дополнений , не забудь пронумеровать главы вот так (1, 2, 3, 4, 5, 6) , а под главы пронумеруй так (1.1 1.2, 2.1 2.2 , 3.1 3.2, 4.1 4.2, 5.1 5.2 , 6.1 6.2) , Первая глава и подглавы 1.1 и 1.2 должны быть вводной частью данного доклада и состоять из актуальности рассматриваемой темы и её проблематики, а шестая глава и подглавы 6.1 6.2 должны быть заключением данного доклада и подводить итоги"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll2 = response['choices'][0]['message']['content']
    print(ll2)


if __name__ == "__main__":
    main()
