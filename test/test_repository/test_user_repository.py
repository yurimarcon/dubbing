import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from repository.users_repository import get_user, create_user, get_all_users, update_user
from repository.database import create_table_user

class TestUserRepository(unittest.TestCase):

    def test_create_databases_and_table(self):
        create_table_user()

    def test_create_user (self):
        create_user("user_test", "teste@gmail.com", "1111-1111", "1234", 10, 1)
        user = get_user(1)
        self.assertEqual(user.name, "user_test")

    def test_get_all_users(self):
        users = get_all_users()
        self.assertEqual(len(users), 1)

    def test_update_user(self):
        user = get_user(1)
        user_to_update = {
            "user_id" : 1,
            "name" : "user_test_updated",
            "is_active" : 0
        }
        update_user(user_to_update) 
        user_updated = get_user(1)
        self.assertEqual(user_updated.name, "user_test_updated")
        self.assertEqual(user_updated.is_active, 0)

    def test_z_remove_database(self):
        os.remove("database.db")

if __name__ == '__main__':
    unittest.main()