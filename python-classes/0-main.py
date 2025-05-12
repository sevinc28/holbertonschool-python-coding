#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))  # Should print <class '0-square.Square'>
print(my_square.__dict__)  # Should show {'_Square__size': 3}

try:
    print(my_square.size)  # Will raise AttributeError because 'size' is not directly accessible
except Exception as e:
    print(e)

try:
    print(my_square.__size)  # Will raise AttributeError because '__size' is private and name-mangled
except Exception as e:
    print(e)
