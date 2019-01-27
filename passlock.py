class Users:

    """
    Class that generates instances of user data
    """
    users_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        Users.users_list.append(self)

    @classmethod
    def users_exist(cls, user_name):
        """
        Method to check if username exists
        """
        for user in cls.users_list:
            if user.user_name == user_name:
                return True
            return False

    @classmethod
    def authenticate_user(cls, user_name, password):
        """
        Method to check whether the username and password matches
        """

        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return user


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



