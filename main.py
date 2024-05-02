import sqlite3

from login_register import login_register
from notes import makeNote

def connect_to_db_users() -> all:
    db = sqlite3.connect('users.db')
    cur = db.cursor()
    try:
        cur.execute('CREATE TABLE users(login, password)')
    except:
        pass

    return db, cur

def connect_to_db_notes(login):
    db = sqlite3.connect('notes.db')
    cur = db.cursor()

    try:
        cur.execute(f'CREATE TABLE {login} (note)')
    except:
        pass

    return db, cur

def main():
    db, cur = connect_to_db_users()
    login = login_register(db, cur)
    users = cur.execute("SELECT login, password FROM users ORDER BY login")
    print('Список пользователей:')
    print([user for user in users])
    db, cur = connect_to_db_notes(login)

    if login:
        print(f'\nВЫ ВОШЛИ ПОД ИМЕНЕМ {login}')
        makeNote(login, db, cur)



if __name__ == '__main__':
    main()