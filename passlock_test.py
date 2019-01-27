import unittest
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
        self.new_users = Users("Nimo", "homeboys123")
        self.new_credentials = Credentials("Instagram", "just_nimo", "homeboys123")

    def test

