from icecream import ic
from getpass import getpass

def login(login) -> bool:
    users = cur.execute("SELECT login, password FROM users ORDER BY login")
    users = [user for user in users]
    logins = [user[0] for user in users]

    if (login in logins) is True:
        return True
    else:
        return False

def password(login_try, password_try) -> bool:
    users = cur.execute("SELECT login, password FROM users ORDER BY login")

    users = [user for user in users]

    for _user in users:
        if _user[0] == login_try:
            password = _user[1]
    if password_try == password:
        return True
    else:
        return False

def get_password() -> str:
    while True:
        password = getpass('Придумайте пароль: ')
        password_confurm = getpass('Подтвержите пароль: ')

        if password == password_confurm:
            break
        print('Попробуйте снова!')
    return password

def get_login() -> str:
    while True:
        new_login = input('Придумайте логин: ')
        if not login(new_login):
            break
        print('Такой логин уже сущестует!\nПопробуйте снова\n')
    return new_login

def add(login, password) -> None:
    cur.execute(f"""INSERT INTO users VALUES
                    ('{login}', '{password}')""")
    db.commit()


def login_user():
    login_try = input('Введите логин: ')
    password_try = getpass('Введите пароль: ')

    if login(login_try):
        if password(login_try, password_try):
            print('LOGGED IN')
            return login_try
        else:
            print('INCORRECT PASSWORD')
    else:
        print('Пользователя не существует!')
        

def login_register(dbb, curr) -> str:
    global cur
    global db
    cur = curr
    db = dbb

    match input('Вход - 1, Регистрация - 2\n'):
        case '1':
            mew_login = login_user()
            if mew_login:
                return mew_login

        case '2':
            new_login = get_login()
            new_password = get_password()
            add(new_login, new_password)
            return new_login

    
