
class Credentials:

    """
    Class that generates instances of credential data
    """

    credentials_list = []

    def __init__(self, acc_name, acc_username, acc_password):
        self.acc_name = acc_name
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_credentials(self):

        """
        Function that adds credentials into credential list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        Delete credentials saved from credential list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        Method to display all credentials
        """
        return cls.credentials_list

    @classmethod
    def find_by_account_name(cls, acc_name):
        """
        Finds credential details using account name
        """
        for found in cls.credentials_list:
            if found.acc_name == acc_name:
                return found

    @classmethod
    def credentials_exist(cls, acc_name):
        """
        Method that checks if credentials exist
        """
        for account in cls.credentials_list:
            if account.acc_name == acc_name:
                return account

    # @classmethod
    # def copy_acc_password(cls, acc_name):
    #     account_found = Credentials.find_by_account_name(acc_name)
    #     pyperclip.copy(account_found.acc_password)
