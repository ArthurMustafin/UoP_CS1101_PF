# source https://www.youtube.com/watch?v=husPzLE6sZc&t
print("LESSON 1: INTRODUCTION TO PROGRAMS DATA TYPES AND VARIABLE")
print("Example one:")
print(3+7)
print(type(3+7))
print(2-1)
print("this is a chunk of text")
print(type("this is a chunk of text"))

print("Example two:")
a = 3 + 5
b = a * a - a - 1
c = a * b
print(c)

print("Example three:")
a = -6                      # previous value erased
b = a * a - a - 1
c = a * b
print(c)

print("Example four:")
a = -6
b = a * a - a - 1
c = a * b
if a < 0:
    print(c)
else:
    print(c-a)

print("Example five:")
a = 9
b = a * a - a - 1
c = a * b
if a < 0:
    print("a<0")
    print(c)
else:
    print("a is not less than 0")
    print(c-a)
print("we are done with the program")

# source https://www.youtube.com/watch?v=iZAtkS0F-Zo
print("LESSON 2: FUN WITH STRINGS")
print("Example one:")
a = "My first test string"
b = 'Another test string that I have defined'
c = "This is sal's string"
d = 'My favourite word is "asparaus", what is yours?'
math_string = "3+4*2"
expression_string = "a+' '+b+' tiger'"

print(len(math_string))
print(len(a))
a_with_b = a + " " + b
b_with_a = b + a
print(a_with_b)
print(b_with_a)
new_string = math_string + expression_string
print(new_string)

e = b.split(' ')
f = b.split('t')
g = math_string.find('*')
h = math_string.find('3')
c.replace('i', 'o')
c = c.replace('i', 'o')
j = eval(math_string)           # run an operation inside the string
k = eval(math_string + '1')     # 3+4*21
l = eval(expression_string)     #
print(e, f, g, h, c, j, k, l)









