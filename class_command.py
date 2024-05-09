from classes import *


class Commands(Tasks):
    def init(self) -> None:
        pass


    def __str__(self) -> str:  # в строчном представлении выводит инфо о командах
        return ''' --lt  -  просмотреть созданные задачи\n --adt  -  добавление задачи\n --up  -  обновление статуса задачи
 --inf  -  информация о доступных командах\n --ex  -  выход из программы'''


    def lt(self):  # команда lt(просмотр созданных задач)
        id = input('Введите id: ')  # запрашиваем id
        if 0 < int(id) <= self.count_tusk():  # если в диапозоне
            id = int(id)
        else:  # если введен id не целое число или не вдиапозоне, то будем выводить весь список
            id = False
        print(self.list_tasks(id))  # выводим на экран список


    def adt(self):  # команда adt(дабвление задачи в список) 
        try:
            tusk = input('Введите задачу: ')  # ввод текста задачи
            status = input('Введите статус задачи: ')  # ввод статуса, можно оставить пустым, тогда дефолтным заполнится
            if status:  # если статус был введен
                self.adder_tusk(tusk, status)  # записывваем задачу
            else:  # если статус не был введен
                self.adder_tusk(tusk)  # записываем задачу
            print('Задача успешно добавлена.\n')
        except:  # если вдруг что-то погло не так
            print('Что-то пошло не так.\n')


    def up(self):  # команда up(обновления статуса задчи)
        print()
        print(self.list_tasks(), '\n')  # выводим весь список задач, чтобы можно было узнать точный ноьмер нужной задачи

        while True:  # итерация, до момента пока не будет введено id целое число и в диапозоне существующих задача
            id = input('Введи номер задачи: ')
            if  0 < int(id) <= self.count_tusk():
                break
            else:  # если неудовлетворяет по кругу 
                print('id должен быть целым числом и находится в списке')
                continue

        status = input('Введите новый статус задачи: ')  # ввод нового статуса
        try:
            self.updater(id, status)  # обновляем статус
            print('Статус успешно обновлен')
        except:
            print('Что-то пошло не так')


        
        



