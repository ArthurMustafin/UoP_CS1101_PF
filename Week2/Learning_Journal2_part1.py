import math

r1 = int(input("What is the radius of the first sphere? "))
r2 = int(input("What is the radius of the second sphere? "))
r3 = int(input("What is the radius of the third sphere? "))


def print_volume(r):
    volume = 4 / 3 * math.pi * r ** 3
    print("Volume of the sphere: ", "%.2f" % volume)


print_volume(r1)
print_volume(r2)
print_volume(r3)


# r1 = int(input("What is the radius of the first sphere? "))
# r2 = int(input("What is the radius of the second sphere? "))
# r3 = int(input("What is the radius of the third sphere? "))
def print_volume(r):
    volume = 4 / 3 * math.pi * r ** 3
    print("Volume of the sphere: ", "%.2f" % volume)


print_volume(5)
print_volume(6)
print_volume(7)

# pi = 3.1415926535897932
# r = 5
# volume = 4/3 * pi *r**3 # better to use float, but Python3 works with fractions
# print(volume)
