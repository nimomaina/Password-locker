#!/usr/bin/env python3.6

from passlock import Users
from passlock import Credentials
import getpass
import random
import string


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


def delete_credential(acc_name):
    """
    Function that deletes credentials
    """
    return Credentials.delete_credentials(acc_name)


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


def pw_gen(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


def main():
    print("Hey, Welcome to Password Locker. Enter username")

    user_name = input("")
    password = getpass.getpass('Password:\n')
    create_user(user_name, password)

    while True:

        print("Use these short codes: dc - display credentials, ac - add credentials, rc - del credentials, ex - exit ")
        print("." * 80)
        credential_code = input(" ")
        if credential_code == 'ac':
            print("Please enter the account like Instagram etc")
            print("-"*30)
            acc_name = input(" ")
            print(f"Please enter username for {acc_name}")
            print("-" * 30)
            acc_username = input()

            pass_code = input(" Use 'gp' to generate password, 'mp' to manually input password")
            if pass_code == 'gp':
                acc_password = pw_gen()
                create_credentials(acc_name, acc_username, acc_password)
                print("\n")
                print(f"Your password is {acc_password}")
            elif pass_code == 'mp':
                acc_password = getpass.getpass('Password:')
                create_credentials(acc_name, acc_username, acc_password)
                print("\n")
                print(f"Your password is {acc_password}")
        elif credential_code == 'dc':
            pass_word = getpass.getpass("Enter your password?\n")
            if pass_word == password:
                if display_credentials():
                    for acc in display_credentials():
                        print("-" * 6, display_credentials().index(acc) + 1, "-" * 6, "\n")
                        print(f"Account name is {acc.acc_name}\n")
                        print(f"Username is {acc.acc_username}\n")
                        print(f"Password is {acc.acc_password}\n")
                else:
                    print("You have no passwords\n")
            else:
                print("Wrong password. You can't view the passwords. Try again\n")
        elif credential_code == 'rc':
            pass_word = getpass.getpass("Enter your password?\n")
            if pass_word == password:
                acc_name = input("Kindly input the account")
                if check_existing_credentials(acc_name):
                    delete_credential(acc_name)
                    print(f"Successfully deleted {acc_name}")

        elif credential_code == "ex":
            print("I hope this app helped you. Bye")
            break


if __name__ == '__main__':

    main()

