# defining a function to print a blank line
def new_line():
	print('.')
	
# defining a function to print three blank lines
def three_lines():
	new_line()
	new_line()
	new_line()
	
# defining a function to print nine blank lines
def nine_lines():
	three_lines()
	three_lines()
	three_lines()
	
# defining a function to print twenty-five blank lines
def clear_screen():
	nine_lines()
	nine_lines()
	three_lines()
	three_lines()
	new_line()
	
# printing nine lines to console
print("Printing nine lines")
nine_lines()

# printing twenty-five lines to console
print("Calling clearScreen()")
clear_screen()
