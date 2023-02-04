'''Password Generator using secrets and string modules to generate a strong passwords'''
import secrets  # obtains all possible letters, digits, and special characters
import string  # obtain cryptographically secure passwords

# function to create password at least 10 characters long


def create_pw(pw_length=10):
    letters = string.ascii_letters  # contains all letters a-z
    nums = string.digits  # for digits in the pw
    characters = string.punctuation  # special characters

    alphabet = letters + nums + characters  # add char in pw together
    pwd = ''
    strong_pw = False
    while not strong_pw:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))
        if (any(char in characters for char in pwd) and sum(char in nums for char in pwd) >= 2):
            strong_pw = True
    return pwd


if __name__ == '__main__':
    print(create_pw())
