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
        self.assertEqual(len(User.users_list), 3)
        
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
        
        def setUp(self):
	        '''
		    Function to test creation of  an account's details before each test
		    '''
	        self.new_details = Details(
	            'Dennis', 'twitter', 'Kiplangat', 'kiplangat18')
        def test__init__(self):
            """
            Test to check if initialization or creation is well done.
            """
            self.assertEqual(self.new_details.user_name, 'Dennis')
            self.assertEqual(self.new_details.site_name, 'twitter')
            self.assertEqual(self.new_details.account_name, 'Kiplangat')
            self.assertEqual(self.new_details.password,'kiplangat18')
        
        
        def test_save_details(self):
            """
            Test to check if the newly created details are saved correctly
            """
            self.new_details.save_details()
            facebook=Details('Dennis', 'Facebook','Kiplangat', 'kiplangat18')
            facebook.save_details()
            self.assertEqual(len(Details.details_list),2)
            
        def tearDown(self):
            """
            Funtion to clear the details list after every test.
            
            """
            Details.details_list = []
            User.users_list = []
            
            
            
        def test_display_details(self):
            """Test to check if the display details method, display the correct details"""
            self.new_details.save_details()
            twitter = Details('Dennis', 'Facebook', 'Kiplangat', 'kiplangat18')
            twitter.save_details()
            gmail = Details('Amos', 'Gmail', 'amos', 'kiplangat18')
            gmail.save_details()
            self.assertEqual(
                len(Details.display_details(twitter.user_name)), 2)








if __name__ == '__main__':
	unittest.main()
