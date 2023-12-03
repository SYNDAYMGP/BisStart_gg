
#---------подчищаем лишние------>(всё что до первой гл1)-----------
with open('1.txt', 'r', encoding=x) as f:
    lines = f.readlines()
index = -1
for i, line in enumerate(lines):
    if "1.1" in line:
        index = i
        break
if index > 1:
    del lines[:index-2]
with open('1.txt', 'w') as f:
    f.writelines(lines)





#---------подчищаем лишние------>(всё что после гл(6.2))-----------

# Открываем файл для чтения
with open('1.txt', 'r') as file:
    lines = file.readlines()
# Ищем строку с числом 6.2
index_6_2 = -1
for i, line in enumerate(lines):
    if '6.2' in line:
        index_6_2 = i
        break
# Если строка с числом 6.2 найдена, ищем следующую пустую строку
if index_6_2 != -1:
    index_empty_line = -1
    for i in range(index_6_2 + 1, len(lines)):
        if lines[i].strip() == '':
            index_empty_line = i
            break
    # Если пустая строка найдена, удаляем все строки после неё
    if index_empty_line != -1:
        lines = lines[:index_empty_line]

        # Записываем изменения обратно в файл
        with open('1.txt', 'w') as file:
            file.writelines(lines)
            print("Операция успешно выполнена.")
    else:
        print("Пустая строка после строки с числом 6.2 не найдена.")
else:
    print("Строка с числом 6.2 не найдена в файле.")





#--------------ЗАПИСЬ ГЛ И ПОДГЛ В ПЕРЕМЕННЫЕ--------------
# Открываем файл для чтения
with open('1.txt', 'r', encoding=x) as file:
    # Инициализируем переменные
    current_variable = ""
    ww_vars = []
    # Читаем файл построчно
    for line in file:
        # Проверяем, содержит ли строка цифру
        if any(char.isdigit() for char in line):
            # Если переменная не пуста, сохраняем ее в список переменных
            if current_variable.strip():  # Добавлена проверка на пустоту
                ww_vars.append(current_variable)
            # Создаем новую переменную и добавляем текущую строку с цифрой
            current_variable = line
        else:
            # Добавляем текущую строку с текстом к текущей переменной
            current_variable += line
    # Добавляем последнюю переменную в список (если она не пуста)
    if current_variable.strip():  # Добавлена проверка на пустоту
        ww_vars.append(current_variable)
# Выводим результат
for i, variable in enumerate(ww_vars, 1):
    print(f"ww_vars[{i-1}]:\n{variable}")





#-----СОЕДИНЕНИЕ ШАБЛОНА С РЕФЕРАТОМ
from docx import Document

# Открываем файлы
doc = Document('1.docx')
with open('2.txt', 'r') as file:
    text = file.read()
# Добавляем текст в документ
doc.add_paragraph(text)
# Сохраняем изменения
doc.save('1.docx')








#-----СОЕДИНЕНИЕ ШАБЛОНА С РЕФЕРАТОМ + Сохраняем документ с изменениями шрифта
import docx
from docx.shared import Pt
from docx import Document
import chardet
# Открываем файлы с явным указанием кодировки (в данном случае UTF-8)
with open('2.txt', 'rb') as file:
    result = chardet.detect(file.read())
# Открываем файлы с определенной кодировкой
with open('2.txt', 'r', encoding=result['encoding']) as file:
    text = file.read()
# Добавляем текст в документ
doc = Document('shablon.docx')
doc.add_paragraph(text)
# Сохраняем изменения
doc.save('shablonDOP.docx')
# Открываем документ с добавленным текстом
document = docx.Document('shablonDOP.docx')
# Изменяем стиль по умолчанию для всего документа
for paragraph in document.paragraphs:
    for run in paragraph.runs:
        font = run.font
        font.name = 'Times New Roman'
        font.size = Pt(14)
# Сохраняем документ с изменениями шрифта
document.save('REFERAT.docx')
print('Шрифт в файле успешно изменен на Times New Roman 14pt')

