#!/usr/bin/env python3.6

from passlock import Users
from passlock import Credentials


def create_user(user_name, password):
     """
     Creates a new user when they login
     """
     new_user = Users(user_name, password)
     return new_user


def save_users(user):
    """
    Function to save contact
    """
    user.save_user()


def check_exist_user(user_name):
    """
    Funtion to check for existing users
    :param user_name:
    :return: Boolean
    """
    return Users.users_exist(user_name)


