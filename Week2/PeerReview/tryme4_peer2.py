#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ice_z
#
# Created:     20/04/2021
# Copyright:   (c) ice_z 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def new_line ():
    print ('.')

def three_lines ():
    new_line ()
    new_line ()
    new_line ()

def nine_lines ():
    three_lines ()
    three_lines ()
    three_lines ()

def clear_screen ():
    nine_lines ()
    nine_lines ()
    three_lines ()
    three_lines ()
    new_line ()

print ('Printing nine_lines')
nine_lines ()

print ('\n' + 'Printing clear_screen')
clear_screen ()