'''
Created on Feb. 19, 2022

@author: Anmol Nagpal
'''

from random import randrange

class User:
    username = str()
    password = str()
    phrases_path = str()
    phrases = list()
    acquired_phrases = False
    def __init__(self, username, password, phrases_path):
        self.username = username
        self.password = password
        self.phrases_path = phrases_path
        
    def _get_phrases(self):
        try:
            with open(self.phrases_path) as file:
                self.phrases = [line.rstrip() for line in file]
        except:
            print("---cannot open file---")
            
    def select_phrase(self):
        if not self.acquired_phrases:
            self._get_phrases()
            self.acquired_phrases = True
        try:
            return self.phrases[randrange(len(self.phrases))]
        except:
            print("---list index out of range---")