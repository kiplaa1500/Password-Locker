import unittest
import pyperclip
from user_details import User, Details


class TestUser(unittest.TestCase):
    """
    Test class that defines class behaviours
    Args:
	    unittest.TestCase: helps in creating test cases
    """

    def setUp(self):
        """
        Set up to run before each test case.
        """
        self.new_users = User('Dennis', 'Kiplangat', 'kiplangat18')
    
    def test__init__(self):
        """
        Test for checking if the initialization is well done
        """
        self.assertEqual(self.new_users.first_name, 'Dennis')
        self.assertEqual(self.new_users.last_name, 'Kiplangat')
        self.assertEqual(self.new_users.password, 'kiplangat18')
    
    def test_save_user(self):
        '''
		Test to check if the new users information is saved into the users list
		'''
        self.new_users.save_user()
        self.assertEqual(len(User.users_list), 1)
        
class TestDetails(unittest.TestCase):
        """
        Test that checks details behaviour.
        """

        def test_check_user(self):
            """
            Funtion to check whether the log in deatils is working properly
            """
            self.new_users = User('Dennis', 'Kiplangat', 'kiplangat18')
            self.new_users.save_user()
            user2 = User('Enock', 'kip', 'mankip')
            user2.save_user()

            for user in User.users_list:
                if user.first_name == user2.first_name and user.password == user2.password:
                   current_user = user.first_name
            return current_user


if __name__ == '__main__':
	unittest.main()
