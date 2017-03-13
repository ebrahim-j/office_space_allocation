"""
This is the interactive Office Space Allocation command line interface
Usage:
	Dojo create_room <room_type> <room_names>
	Dojo add_person <person_name> <email_address> <role> [<wants_accomodation>]
	Dojo print_room <room_name>
	Dojo print_allocations [--o=filename]
	Dojo print_unallocated [--o=filename]
"""

import cmd

from app.dojo import Dojo
from text_styles import text_format

from docopt import docopt, DocoptExit	
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
	cprint(figlet_format('Dojo Space', font='roman'), 'magenta', 
		attrs=['blink'])
	print("Welcome to the Dojo Space Allocator." + 
		"Here is a list of commands for your use " + 
		"Type 'help' anytime to access available commands")
	cprint(__doc__, 'blue')


class Dojo_Interface(cmd.Cmd):
	launch()
	prompt = 'Dojo->>'

	dojo_space = Dojo()


	@docopt_cmd
	def do_create_room(self, arg):
		"""Usage: create_room <room_type> <room_names> """
		roomtype = arg["<room_type>"]
		roomnames = ''.join(arg["<room_names>"]).split(',')
		

		for roomname in roomnames:
			print(self.dojo_space.create_room(roomtype, roomname))
		

	@docopt_cmd
	def do_add_person(self, arg):
	 	"""Usage: add_person <person_name> <email_address> <role> [<wants_accomodation>]"""
	 	name = arg["<person_name>"]
	 	email_address = arg["<email_address>"]
	 	role = arg["<role>"]
	 	accomodation_option = arg["<wants_accomodation>"]

	 	if role== "Staff" and accomodation_option == "y":
	 		print (text_format.CRED + "\nWARNING! Staff cannot be allocated accomodation space\n" +text_format.CEND)
	 		return	

	 	print (self.dojo_space.add_person(name, email_address, role, accomodation_option))

	
	@docopt_cmd
	def do_print_room(self, arg):
		"""Usage: print_room <room_name>"""
		roomname = arg["<room_name>"]

		print (self.dojo_space.print_room(roomname))


	@docopt_cmd
	def do_print_allocations(self, arg):
		"""Usage: print_allocations [--o=filename]"""
		filename = arg["--o"]

		print(self.dojo_space.print_allocations(filename))


	@docopt_cmd
	def do_print_unallocated(self, arg):
		"""Usage: print_unallocated [--o=filename]"""
		filename = arg["--o"]

		print(self.dojo_space.print_unallocated(filename))


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
