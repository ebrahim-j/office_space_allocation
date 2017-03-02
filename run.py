"""
This is the interactive Office Space Allocation command line interface
Usage:
	dojo create_room <room_type> <room_name>
	dojo add_person <person_name> <FELLOW|STAFF> [wants_accomodation]
	dojo (-i | --interactive)
	dojo (-h | --help | --version)
Options:
	-i, --interactive Interactive Mode
	-h, --help Shows the available commands for dojo
"""

import cmd
from docopt import docopt, DocoptExit
from app.dojo import Dojo	
from pyfiglet import figlet_format
from termcolor import cprint



def docopt_cmd(func):
	"""
   	This decorator is used to simplify the try/except block and pass the result
   	of the docopt parsing to the called action.
   	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__,arg)

		except DocoptExit as e:
			 # The DocoptExit is thrown when the args do not match.
			 # We print a message to the user and the usage block.

			 print('Invalid Command!')
			 print(e)
			 return

		except SystemExit:
			# The SystemExit exception prints the usage for --help
			# We do not need to do the print here.

			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn


def launch():
	cprint(figlet_format('Dojo Space Allocator', font='poison'), 'green', 
		attrs=['blink'])
	print("Welcome to the Dojo Space Allocator." + 
		"Here is a list of commands for your use " + 
		"Type 'help' anytime to access available commands")
	cprint(__doc__, 'blue')


class Dojo_Interface(cmd.Cmd):
	launch()
	prompt = 'DSA->>'

	 dojo_space = Dojo()


	@docopt_cmd
	def do_create_room(self, arg):
		"""Usage: create_room <room_type> <room_name> """
		roomtype = arg["<room_type>"]
		roomname = arg["<room_name>"]
		pass

	@docopt_cmd
	def do_add_person(self, arg):
	 	"""Usage: add_person <person_name> <FELLOW|STAFF> [wants_accomodation]"""
	 	name = arg["<person_name>"]
	 	role = arg["<FELLOW|STAFF>"]
	 	choose_acc = arg["<wants_accomodation>"]
	 	pass

	def do_quit():
		"""Quits interactive mode"""
		print ('...soon I shall become a memory waiting to be erased')
		print ('... Goodbye!')
		exit()


if __name__ == '__main__':
	try:
		Dojo_Interface().cmdloop()
	except KeyboardInterrupt:
		print ('Exiting...')
