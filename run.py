#!/usr/bin/env python3.6

from user import Users
from credential import Credentials
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


def check_exist_user(characters):
    """
    Function to check for existing users
    """
    return Users.users_exist(characters)


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
    # global acc_password, acc_name
    print("*"*60)
    print(" "*20, "WELCOME TO PASSWORD LOCKER", " "*20, )
    print("*"*60)
    print("\n")

    print("What is your name?\n")
    user_name = input()
    print("\n")
    print(f"Hello {user_name}.\n")

    while True:
        print("." * 80)
        print("""\nUse these short codes: 
        ca - create account
        ac - add credentials
        dc - display credentials
        dl - delete account
        ex - exit """)
        print("." * 80)
        credential_code = input(" ")
        if credential_code == 'ca':
            print("Great! Enter the following:")
            print("*" * 30)

            print(" user name:\n")
            user_name = input()
            print("_" * 30)

            print("\nPassword:\n")
            password = input()
            print("_" * 30)
            save_users(create_user(user_name, password))
            print("\n")
            print(f" Account for user ( {user_name} ) created.\n")

        elif credential_code == 'ac':
            print("\nPlease log in to your account")
            print("*" * 40)
            print(" user name:\n")
            user_name = input()
            print("_" * 30)

            print("\nPassword:\n")
            password = input()
            print("_" * 30)
            if check_exist_user(password):
                print("\n", " "*20, f"Welcome back {user_name}", " "*20,)
                print("Add New Credentials")
                print("*" * 40)

                print("\nAccount name:\n")

                acc_name = input()

                print(f"\nUsername for {acc_name}:\n")
                acc_username = input()

                print("""Choose one of these: 
                       gp - generate password
                       mp - manually input passwords
                       """)
                pass_code = input(" ")

                if pass_code == 'gp':
                    acc_password = pw_gen()
                    print("\n")
                    print(f"Your password is {acc_password}")
                    print("." * 80)
                elif pass_code == 'mp':
                    acc_password = getpass.getpass('Password:')
                    print("\n")
                    print(f"Your password is {acc_password}")
                    print("." * 80)

                save_credential(create_credentials(acc_name, acc_username, acc_password))
                print("\n")
                print(f"""Successfully created Account:
                            {acc_name}
                            {acc_username}
                            {acc_password}""")

            else:
                print("Authentication error. Please Try again.\n")
                print("*" * 50)
                print(" user name:\n")
                user_name = input()
                print("_" * 30)

                print("\nPassword:\n")
                password = input()
                print("_" * 30)
                if check_exist_user(password):
                    print("\n", " "*20, f"Welcome back {user_name}", " "*20,)
                else:
                    print("Please create an account first.\n")

        elif credential_code == 'dc':
            print("\n", " " * 20, "List of accounts you have saved", " " * 20, )

            if display_credentials():
                for credential in display_credentials():

                    print(f"""Account:
                            {credential.acc_name}
                            {credential.acc_username}
                            {credential.acc_password}""")
            else:
                print("\n Sorry you don't have any accounts")
       
        elif credential_code == "dl":
            print("Enter account name you want to delete")
            print("*"*30)
            search_account = input()
            if check_existing_credentials(search_account):
                search_credential = find_credentials(search_account)
                print(f"Account: {search_credential.acc_name}\nUsername: {search_credential.acc_username}\nPassword: {search_credential.acc_password}")
                print(f"Confirm you want to delete account {search_credential.acc_name} ? \ny\nn")
                answer = input().lower()

                if answer == 'y':
                    delete_credential(search_credential)
                    print("Account has been deleted")
        elif credential_code == "ex":
            print("Sad to see you leave (^__^) \n I hope this app helped you. Bye")
            break


if __name__ == '__main__':

    main()

