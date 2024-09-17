from  sqlite4  import  SQLite4
from entities.user import User

database = SQLite4("database.db")

database.connect()

def create_user(name, email, tel, password, credits, is_active):
    database.execute(f'''
        INSERT INTO Users ( 
            name, 
            email,
            tel,
            password,
            credits,
            is_active
        ) VALUES (
            "{name}",   
            "{email}",
            "{tel}",
            "{password}",
            {credits},
            {is_active}
            )
    ''')

def get_user(user_id):
    rows = database.select("Users", columns=[], condition=f"user_id = {user_id}")
    return User(*rows[0])

def get_all_users():
    return database.select("Users")

def update_user(user):
    database.update("Users", data=user, condition=f"user_id = {user['user_id']}")

if __name__ == '__main__':
    main()