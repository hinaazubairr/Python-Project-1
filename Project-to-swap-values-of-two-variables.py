# SECTION # 2 : EXAMPLE-8 -- -- TO SWAP VALUES OF TWO VARIABLES

# Variables 'a' and 'b' each have associated values. Swap them, so that 'a' becomes associated with b's original value, and 'b' becomes associated with it’s original value. You can use two more variables i_temp and j_temp.

# Given two already defined variables, i and j, write a statement that swaps their associated values.
# initial values

a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

# use temporary variables
i_temp = a
j_temp = b

# swap
a = j_temp
b = i_temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
