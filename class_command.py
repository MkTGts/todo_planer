from classes import *


class Commands(Tasks):
    def init(self) -> None:
        pass


    def __str__(self) -> str:  # в строчном представлении выводит инфо о командах
        return ''' --ex  -  выход из программы\n --adt  -  добавление задачи\n --up  -  обновление статуса задачи
 --lt  -  просмотреть созданные задачи\n --dl  -  удаляет задачу\n --inf  -  информация о доступных командах'''


    def lt(self, id=False):  # команда lt(просмотр созданных задач)       
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
                print('id должен быть целым числом и находиться в диапозоне')
                continue

        status = input('Введите новый статус задачи: ')  # ввод нового статуса
        try:
            self.updater(id, status)  # обновляем статус
            print('Статус успешно обновлен')
        except:
            print('Что-то пошло не так')

        
    def dl(self):  # команда удаления задачи
        print()
        print(self.list_tasks(), '\n')  # выводим список задач, что-бы посмотреть номер

        while True:
            id = input('Введите номер задачи: ')
            if 0 < int(id) <= self.count_tusk():
                break
            else:
                print('id должен быть целым числом и находиться в диапозоне')
                continue

        self.dellitter(int(id))
        print('Задача удален.\n')


        
        
t = Commands()
t.connecter()
t.lt(3)
t.disconnecter()



