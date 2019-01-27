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

    def test_new_user_creation(self):
        """
        Tests if new users account has been created
        """
        self.new_user.save_user()
        self.assertEqual(len(Users.users_list), 1)


class TestCredentials(unittest.TestCase):

    """
       Test class that defines test cases for the users class behaviours

       Args:
           unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
         Set up method before running tests
        """
        self.new_credentials = Credentials("Instagram", "just_nimo","homeboys123")

    def tearDown(self):
        """
        Clean after running tests
        """
        Credentials.credentials_list = []

    def test_save_credentials(self):
        """
        Test to check if credentials is added to credentials list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_delete(self):
        """
        Test to check if credentials are removed from credential list
        """
        self.new_credentials.save_credentials()
        test_cred = Credentials("Instagram", "just_nimo","homeboys123")
        test_cred.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)