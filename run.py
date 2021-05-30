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
