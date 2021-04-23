                        # 42 = n, mistake can't assign to literal
x = y = 1               # operation is allowed
print(x)
print(y)
                        # The semicolon is legal. But that doesn’t mean that you should use it.
                        # z = xy is not allowed
print("Exercise 2.2.1")
pi = 3.1415926535897932
r = 5
volume = 4/3 * pi *r**3 # better to use float, but Python3 works with fractions
print(volume)

print("Exercise 2.2.2 my solution")
cover_price = 24.95
bookstore_price = cover_price - (cover_price * 0.4)
cost_with_shipping_first = bookstore_price + 3
cost_with_shipping_other = bookstore_price + 0.75
wholesale_cost = (cost_with_shipping_first + (cost_with_shipping_other * 59))
print("Total wholesale cost is", "%.2f" % wholesale_cost, "USD")

print("Exercise 2.2.2 other solution")
cover_price = 24.95
number_of_books = int(input("How many books do you want to order at wholesale? "))

def ship_cost(number_of_books):
    if number_of_books == 1:
        return (number_of_books * 3) # Cost of shipping one book is $3
    else:
        return (3 + (number_of_books - 1) * 0.75) # Each additional copy of the book is $0.75 to ship

def discounted_price(number_of_books):
    return(cover_price - (cover_price * .4)) # There is a 40% discount on wholesale book sales

def wholesale_cost(number_of_books):
    return ((discounted_price(number_of_books) * number_of_books) + ship_cost(number_of_books))

print("The cost of buying and shipping", number_of_books, "books is $",round(wholesale_cost(number_of_books), 2))


print("Exercise 2.2.3")
a = (6 + (52/60))
pace_1 = (8 + (15/60))
pace_2 = (7 + (12/60))
time_1 = (1 * pace_1)
time_2 = (3 * pace_2)


def life_in_hours(time):
    hours = (time*365*24)
    print(hours)
life_in_hours(10)