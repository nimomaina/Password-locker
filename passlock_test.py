import unittest
import pyperclip
from passlock import Users
from passlock import Credentials


class TestUsers(unittest.TestCase):

    """
       Test class that defines test cases for the users class behaviours

       Args:
           unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = Users("Nimo", "homeboys123")

    def tearDown(self):
        """
        cleans up after every test has been done
        """
        Users.users_list = []

    def test_init(self):
        """
        Test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name, "Judy")
        self.assertEqual(self.new_user.password, "homeboys123")

    def test_user_account_create(self):
        """
        Tests if new users account has been created
        """
        self.new_user.save_user()
        self.assertEqual(len(Users.users_list), 1)




