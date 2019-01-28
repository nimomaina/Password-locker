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
    Function to check for existing users
    :param user_name:
    :return: Boolean
    """
    return Users.users_exist(user_name)


def authenticate_user(user_name, password):
    """
    Function to authenticate users when they login
    :param user_name:
    :param password:
    """
    return Users.authenticate_user(user_name, password)


def create_credentials(acc_name, acc_username, acc_password):
    """
    Function that creates new credentials
    :param acc_name:
    :param acc_username:
    :param acc_password:
    :return: newly created credential
    """
    new_credential = Credentials(acc_name, acc_username, acc_password)
    return new_credential


def save_credential(credential):
    """
    Function that adds credentials to credential list
    """
    credential.save_credentials()


def delete_credential(credential):
    """
    Function that deletes credentials
    """
    credential.delete_credentials()


def find_credentials(acc_name):
    """
    Function that finds an account using the account name
    """
    return Credentials.find_by_account_name(acc_name)


def check_existing_credentials(acc_name):
    """
    Function that checks if a credential actually exists
    """
    return Credentials.credentials_exist(acc_name)


def display_credentials():
    """
    Function that returns all saved credentials
    """
    return Credentials.display_credentials()


