# tests/test_user.py

import unittest
from app.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        User.users = {}

    def test_register(self):
        self.assertTrue(User.register("user1", "password1"))
        self.assertFalse(User.register("user1", "password1"))  # Duplicate

    def test_login(self):
        User.register("user1", "password1")
        self.assertTrue(User.login("user1", "password1"))
        self.assertFalse(User.login("user1", "wrongpassword"))
        self.assertFalse(User.login("user2", "password1"))

if __name__ == '__main__':
    unittest.main()
