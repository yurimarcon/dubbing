from  sqlite4  import  SQLite4
from entities.user import User
from datetime import datetime

database = SQLite4("database.db")

database.connect()

def create_user(name, email, tel, password, credits, is_active ):
    database.execute(f'''
        INSERT INTO Users ( 
            name, 
            email,
            tel,
            password,
            credits,
            is_active,
            created_date,
            last_update
        ) VALUES (
            "{name}",   
            "{email}",
            "{tel}",
            "{password}",
            {credits},
            {is_active},
            "{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}",
            "{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}"
            )
    ''')

def get_user_by_id(user_id):
    rows = database.select("Users", columns=[], condition=f"user_id = {user_id}")
    return User(*rows[0])

def get_user_by_name(user_name):
    try:
        rows = database.select("Users", columns=[], condition=f"name = '{user_name}'")
        return User(*rows[0])
    except:
        return

def get_all_users():
    return database.select("Users")

def update_user(user):
    database.update("Users", data=user, condition=f"user_id = {user['user_id']}")

if __name__ == '__main__':
    main()