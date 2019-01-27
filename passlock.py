class Users:

    """
    Class that generates instances of user data
    """
    users_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        pass


class Credentials:

    """
    Class that generates instances of credential data
    """

    credentials_list = []

    def __init__(self, acc_name, acc_username, acc_password):
        self.acc_name = acc_name
        self.acc_username = acc_username
        self.acc_password = acc_password