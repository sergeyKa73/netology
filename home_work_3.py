# Задание 3
# Модифицируйте программу из задания 2 таким образом, чтобы данные не выводились на экран, а сохранялись в словарь. Ключами в этом словаре должны быть даты, а значениями - соответствующие им задачи.

# Пример ввода программы:
# ```
# Введите дату: Сегодня
# Введите задачу: Выучить Python
# Введите дату: Завтра
# Введите задачу: Разработать TODO-приложение
# Введите дату: Послезавтра
# Введите задачу: Разработать Telegram-бота
# ```
# Это задание не предполагает вывод информации на экран.
key_1,enter_task_1 = map(str, input('Введите дату и задачу через пробел:').split())
key_2,enter_task_2 = map(str, input('Введите дату и задачу через пробел:').split())
key_3,enter_task_3 = map(str, input('Введите дату и задачу через пробел:').split())
dict_todo = dict( a = enter_task_1, b = enter_task_2, c = enter_task_3)
print(dict_todo)