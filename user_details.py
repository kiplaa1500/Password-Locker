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
     
    def save_user(self):
        """
        Function to save a newly created instances.
        """
        User.users_list.append(self)
        
class Details:
        """
        Class for creating account details.
        """
        details_list = []
        user_details_list = []

        @classmethod
        def check_user(cls, first_name, password):
            """
            Its a method to check if the entered password matches the one in user list
            """

            current_user = ''
            for user in User.users_list:
                if (user.first_name == first_name and user.password == password):
                    current_user = user.first_name
            return current_user
        
        def __init__(self, user_name, site_name, account_name, password):
	         '''
	          Method to define the properties for each user object will hold.
	         '''

	     # instance variables
	         self.user_name = user_name
	         self.site_name = site_name
	         self.account_name = account_name
	         self.password = password
          
        def save_details(self):
             """
             Function to save newly created user deatils
             """
             Details.details_list.append(self)

        def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
             """
             Function for generating 8 character password
             """
             gen_pass = ''.join(random.choice(char) for _ in range(size))
             return gen_pass
         
         
        @classmethod
        def display_details(cls, user_name):
	        '''
		    Class method to display the list of details saved
		    '''
	        user_details_list = []
	        for detail in cls.details_list:
		        if detail.user_name == user_name:
			        user_details_list.append(detail)
	        return user_details_list
     
     
    #  method for returning details matching values earlier entered 
        @classmethod
        def find_by_site_name(cls, site_name):
             """
             Method that returns details that matches the feeded one
             """
             for detail in cls.details_list:
                 if detail.site_name == site_name:
                         return detail

