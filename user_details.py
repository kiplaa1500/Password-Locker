import pyperclip
import random
import string

#Variables 

global users_list


class User:
    """
    class that generate new instances of contact
    """
    users_list = []

    def __init__(self, first_name, last_name, password):
     """
     defining properties of our class
     """
     self.first_name = first_name
     self.last_name = last_name
     self.password = password
    
