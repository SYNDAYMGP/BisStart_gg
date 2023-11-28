
#ЗАПИСЬ ГЛ И ПОДГЛ В ПЕРЕМЕННЫЕ


# Открываем файл для чтения
with open('1.txt', 'r', encoding='utf-8') as file:
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
print(ww_vars[15])











