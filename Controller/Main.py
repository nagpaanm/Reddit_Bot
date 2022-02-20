'''
Created on Feb. 19, 2022

@author: Anmol Nagpal
'''
from User.User import User


username = "carnagetabot"
password = "password123"
phrases_path = "../TextFiles/phrases.txt"

if __name__ == '__main__':
    user = User(username, password, phrases_path)
    print(user.select_phrase())
    