# Давайте усложним нашу программу. Сделайте следующие изменения:

#     Заведите 3 списка: today, tomorrow, other (вы можете назвать переменные по-другому).
#     Измените блок кода, который выполняет команду add:

#     Дополнительно запросите у пользователя дату выполнения задачи.
#     В зависимости от введенной даты добавьте задачу в один из списков по следующим правилам:
#         Если пользователь ввел "Сегодня", добавьте задачу в список today.
#         Если пользователь ввел "Завтра", добавьте задачу в список tomorrow.
#         Если пользователь ввел любое другое значение, добавьте задачу в список other.

HELP = '''
help - напечатать справку о программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
exit - напечатать Спасибо за использование! До свидания!
'''
tasks_today = []
tasks_tomorrow = []
tasks_other = []

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
            print(HELP)
    elif command == 'show':
            tasks = tasks_today +  tasks_tomorrow  + tasks_other
            print(tasks)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    elif command == 'add':
        day = input('Введите дату :')
        task = input('Введите название задачи: ')
    elif day == 'Сегодня':
        tasks_today.append(task)
        print('Задача добавлена')
    elif day == 'Завтра':
        tasks_tomorrow.append(task)
        print('Задача добавлена')
    elif day =='Other':
        tasks_other.append(task)
        print('Задача добавлена')
    elif day != 'Сегодня' or day !='Завтра' or day !='Other':
        print('Ведите корректную дату')       
    else:
        print('Неизвестная команда')
        continue

