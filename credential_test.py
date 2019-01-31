import unittest
from credential import Credentials


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
        self.new_credentials = Credentials("Instagram", "just_nimo", "homeboys123")

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

    def test_display_credentials(self):
        """
        Method that returns a list of all credentials saved
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()
