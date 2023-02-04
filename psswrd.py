'''Password Generator using secrets and string modules to generate a strong passwords'''
import secrets  # obtains all possible letters, digits, and special characters
import string  # obtain cryptographically secure passwords

#function to create password at least 10 characters long

def create_pw(pw_length=10):
    letters = string.ascii_letters #contains all letters a-z
    nums = string.digits #for digits in the pw
    characters = string.punctuation #special characters