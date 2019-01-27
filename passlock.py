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
        Delete crediantials saved from credential list
        """
        Credentials.credentials_list.remove(self)

