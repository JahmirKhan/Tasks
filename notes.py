import os
import sqlite3

class ToDoList:
    def __init__(self, login):
        notes = notes_cur.execute(f"SELECT note FROM {login}")
        self.tasks = [note for note in notes]
        self.login = login

        self.viev_tasks()

    def save(self):
        try:
            os.remove('notes')
        except:
            pass
        with open('notes', 'a') as r:
            for i, task in enumerate(self.tasks):
                r.write(f'{i}. {task} \n')

    #добавление значения
    def add_in_list(self):
        print('Исходный список')
        self.viev_tasks()
        new_val = input('Введите задачу\n')
        while new_val in self.tasks:
            new_val = input('Это значение уже существует!\nВведите задачу\n')
        self.tasks.append(new_val)
        print('Измененный список')
        self.viev_tasks()
        self.save()

        notes_cur.execute(f"""INSERT INTO {self.login} VALUES
                        ('{new_val}')""")
        notes_users_db.commit()


    #вывод значений
    def viev_tasks(self):
        print('\nСПИСОК СОХРАНЕННЫХ ЗАДАЧ:')
        for i, task in enumerate(self.tasks):
            print(f'{i+1}. {''.join(task)}')
        print()

    #Удаление значения
    def remove_list(self):

        print('Исходный список')
        self.viev_tasks()
        variants = self.get_valid_val('Какую по номеру задачу вы хотите удалить нафиг?')
        self.tasks.remove(self.tasks[int(variants)])
        print('Измененный список')
        self.viev_tasks()
        self.save()

    def change_list(self):
        print('Исходный список')
        self.viev_tasks()
        variants = self.get_valid_val('Какую по номеру задачу вы хотите изменить?')
        new_val = input('Введите новое значение\n')
        while new_val in self.tasks:
            new_val = input('Это значение уже существует!\nВведите новое значение\n')

        self.tasks[int(variants)] = new_val
        print('Измененный список')
        self.viev_tasks()
        self.save()

    def choose_action(self):
        match input('Выберите действие:\n1 - Добавить в список\n2 - Посмотеть список\n3 - Изменить список\n4 - Удалить из списка\nВаше действие: '):
            case '1':
                 self.add_in_list()
            case '2':
                 print('Исходный список')
                 self.viev_tasks()
            case '3':
                 self.change_list()
            case '4':
                self.remove_list()
            case _:
                pass

    def get_valid_val(self, text):
        variants = input(text)
        while True:
            try:
                return int(variants)
            except:
                variants = input(text)





def makeNote(login, db, cur):
    global notes_cur
    global notes_users_db
    notes_cur = cur
    notes_users_db = db

    somelist = ToDoList(login)

    while True:
        somelist.choose_action()

