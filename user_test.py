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


if __name__ == '__main__':
	unittest.main()
