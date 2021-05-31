#! /usr/bin/env python3
import pyperclip
from user_details import User, Details


def create_user(fname, lname, password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname, lname, password)
	return new_user


def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)
 
 
 
def confirm_user(first_name, password):
	'''
	Function that confirms the existance of the user before creating details 
	'''
	checking_user = Details.check_user(first_name, password)
	return checking_user


def generate_password():
	'''
	Function to generate a password for the user.
	'''
	gen_pass = Details.generate_password()
	return gen_pass


def create_details(user_name, site_name, account_name, password):
	'''
	Function to create a new details.
	'''
	new_details = Details(user_name, site_name, account_name, password)
	return new_details


def save_details(details):
	'''
	Function to save a newly created details
	'''
	Details.save_details(details)


def display_details(user_name):
	'''
	Function to display details saved by a user
	'''
	return Details.display_details(user_name)


def copy_details(site_name):
	'''
	Function to copy a details details to the clipboard
	'''
	return Details.copy_details(site_name)


def main():
	print(' ')
	print('Welcome to Password Locker application.')
	while True:
		print('Use the codes to navigate: \n na-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'na':
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name, last_name, password))
			print(" ")
			print(
				f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'li':
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = confirm_user(user_name, password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print('Navigation codes: \n cc-Create a Details \n dc-Display Details \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your details details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Wrong option entered. Try again.')
						save_details(create_details(
							user_name, site_name, account_name, password))
						print(' ')
						print(
							f'details Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_details(user_name):
							print('Here is a list of all your details')
							print(' ')
							for details in display_details(user_name):
								print(
									f'Site Name: {details.site_name} - Account Name: {details.account_name} - Password: {details.password}')
							print(' ')
						else:
							print(' ')
							print("You don't seem to have any details saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input(
							'Enter the site name for the details password to copy: ')
						copy_details(chosen_site)
						print('')
					else:
						print('Wrong option entered. Try again.')

			else:
				print(' ')
				print('Wrong details entered. Try again or Create an Account.')

		else:
			print(' ')
			print('Wrong option entered. Try again.')
   

if __name__ == '__main__':
	main()
