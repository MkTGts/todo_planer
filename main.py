from class_command import *


print('Это планировщик задач.\n')
cmnd = Commands()
print(cmnd)


while True:
    try:
        cmnd.connecter()  # подключаемся к бд
        cmnd.creater_base()  # проверка на случай если бд еще не создана

        c = input('Введите команду >: ')

        if c == 'ex' or c == 'уч':  # если команда на выход
            print('Выход')
            break
        elif c == 'inf' or c == 'шта':
            print(cmnd)
            continue

        if c[-1] != ')':  # если не подан аргумент
            c += '()'  # добавляем скобки для вызова

        try:
            exec(f'cmnd.{c}')
        except:
            print('Неверная комманда.')
            continue
    except:
        cmnd.disconnecter()
        print('Sorry, error.')
        break


    