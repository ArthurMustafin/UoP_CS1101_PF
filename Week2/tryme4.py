def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()
print("9 lines")
nine_lines()       #printing 9 lines by executing the function

print("25 lines")
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()
clear_screen()      #printing 25 lines by executing the function
