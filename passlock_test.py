
    def test_copy_password(self):
        """
        Test to confirm the password to copy of found account name
        """

        self.new_credentials.save_credentials()
        Credentials.copy_acc_password("Instagram")
        self.assertEqual(self.new_credentials.acc_password.pyperclip.paste())

