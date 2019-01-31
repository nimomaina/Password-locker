
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
    def users_exist(cls, characters):
        """
        Method to check if username exists
        """
        for user in cls.users_list:
            if user.password == characters:
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

