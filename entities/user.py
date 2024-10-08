
class User:
    def __init__(self, user_id, name, email, phone, password, credits, is_active, created_date, last_update):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.credits = credits
        self.is_active = is_active
        self.created_date = created_date
        self.last_update = last_update

    def __repr__(self):
        return f"(user_id={self.user_id}, name='{self.name}', email='{self.email}', phone='{self.phone}', credits={self.credits}, is_active={self.is_active}, created_date='{self.created_date}', last_update='{self.last_update}')"
