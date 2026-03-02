# CHAPTER 5 : NUMBERS
# Python has 2 number types: i.e., int and float.

# INTEGER:
# int (short for integer) is a whole number. It can be either +ve, -ve or 0.
# Examples of integers are: 3200, -84, 2, 197

# FLOAT:
# A float is any number that contains a decimal point. It can be either +ve, -ve or 0.
# Examples of floats are: 7.0, 9.38, 16.001, -35.2



# TYPE() FUNCTION:
# Given any number, the type() function tells you whether it's an int or a float.
# SYNTAX: type(object)

print(type(37))
print(type(4.2))
print(type(98.321))




# TYPE CONVERSION: You can also change the numeric type of a number by converting a number from one type to another. This process is called type conversion
# int(float)
# float(int)

sum = 3.4+2.7
print(sum)
print(type(sum))    # to know what is the type of the sum

sum = int(sum)  # convert the type to int
print(sum)
print(type(sum))    # to know what is the type of the sum


# ARITHMETIC OPERATORS
print(type(40+2.5))         # this is float type
# addition, subtraction or multiplication with int produces an int.
print(type(2+2))            # this is int type


# ORDER OF OPERATIONS (PEMDAS) - Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
print(5*(3**2+5)-8/2)   # 5*(14)-8/2-----------70-8/2-----70-4.0------66.0



cakes= 12
pies= 4
desserts = cakes+pies
print(desserts)



