
from user import Users
import unittest

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
        self.new_user = Users("Judy", "homeboys123")

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

    def test_new_user_creation(self):
        """
        Tests if new users account has been created
        """
        self.new_user.save_user()
        self.assertEqual(len(Users.users_list), 1)

    def test_users_exists(self):
        """
        test_user_exists test case to check if we can return a boolean if we cannot find the user
        """
        self.new_user.save_user()
        test_user = Users("Judy", "homeboys123")
        test_user.save_user()
        user_exists = Users.users_exist("homeboys123")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
