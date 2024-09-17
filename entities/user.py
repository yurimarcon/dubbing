
class User:
    def __init__(self, user_id, name, email, phone, password, credits, is_active):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.credits = credits
        self.is_active = is_active

    def __repr__(self):
        return f"(user_id={self.user_id}, name='{self.name}', email='{self.email}', phone='{self.phone}', level={self.credits}, active={self.is_active})"
