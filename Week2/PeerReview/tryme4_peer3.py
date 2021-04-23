def new_line():          #This means we named the function "new_line" and
    print('.')                # it's going to print '.' when we call the fuction "new_line"
def three_lines():      # This means we named the function "three_lines" and
    new_line()            #it's going to print 'new_line' three times when we call the fuction "three_line"
    new_line()
    new_line()

def nine_lines():       #The process continues like the above
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    print("printing 25 lines")
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print (nine_lines())
print (clear_screen())

