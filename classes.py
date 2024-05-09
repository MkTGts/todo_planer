import sqlite3 as sql


class Tasks():
    def __init__(self) -> None:
        pass


    def connecter(self) -> None:  # коннектер, подключает к бд
        self.con = sql.connect('data/task.db')
        self.curs = self.con.cursor()


    def disconnecter(self) -> None:  # закрывате бд
         self.con.close() 


    def creater_base(self) -> None:  # создает базу, если база еще не существует
        self.curs.execute('''CREATE TABLE IF NOT EXISTS tasks(
                    id INTEGER PRIMARY KEY,
                    info TEXT NOT NULL,
                    status TEXT DEFAULT 'пока нет'
        ) ''')
        self.con.commit()


    def adder_tusk(self, task: str, status='пока нет статуса') -> None:  # добавления задачи
        self.curs.execute('INSERT INTO tasks(info, status) VALUES (?, ?)', (task, status))
        self.con.commit()


    def updater(self, id: int, status: str|int) -> None:  # обновления статуса задачи
        self.curs.execute('''UPDATE tasks
                          SET status=?
                          WHERE id=?''',
                          (status, id))
        self.con.commit()


    def list_tasks(self, id=False) -> str:  # возвращает данные о задачах из бд. если id не указаывается, возвращает весь список задач
        if id:  # если id указан, возвращает по id
            self.curs.execute('''SELECT info, status
                              FROM tasks
                              WHERE id=?''', (id, ))            
            res = self.curs.fetchone()
            return '; статус: '.join(res)

        else:  # если id не указан, возвращает весь список задач
            self.curs.execute('''SELECT *
                              FROM tasks''')     
            ret = []            
            for el in self.curs.fetchall():
                ret.append(f'{el[0]}) {el[1]}; статус: {el[2]}')
            return '\n'.join(ret)        

    
    def count_tusk(self):  # возвращает количество записанных задач
        self.curs.execute('''SELECT id
                          FROM tasks''')
        res = self.curs.fetchall()
        return len(res)
    

t1 = Tasks()
t1.connecter()
print(t1.count_tusk())
t1.disconnecter()

    
    