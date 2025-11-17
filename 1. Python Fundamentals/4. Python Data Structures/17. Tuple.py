# Tuple - ordered, immutable, indexable, faster than lists, hashable (if elements are hashable)
# It's like read-only list.

# Basic Tuple
t = (1, 2, 3)

# Without parentheses:
t = 1, 2, 3

# Single-element tuple
t = (5,)     # COMMA required
t = (5)     # not a tuple, just an integer

# Using tuple():
t = tuple([1, 2, 3])

# Tuples prevent accidental mutations

# Tuples can be dictionary keys
a = {(1,2): "value"}   # valid

# Accessing Tuple Elements
t[0]
t[-1]
t[1:3]
# Slicing returns a new tuple.

# Tuple Packing & Unpacking
# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t

# Extended unpacking
a, *b = (1, 2, 3, 4)
# Output : a = 1, b = [2,3,4]

# Ignoring values
my_tuple = ("apple", "banana", "cherry", "date")
first_fruit, _, third_fruit, _ = my_tuple # Unpack and ignore the second and fourth values

print(f"First fruit: {first_fruit}")
print(f"Third fruit: {third_fruit}")

# Ignoring multiple consecutive values with the * operator
data = (1, 2, 3, 4, 5, 6, 7, 8, 9)
first_val, *_, last_val = data # Unpack and ignore the middle elements

print(f"First value: {first_val}")
print(f"Last value: {last_val}")

# Immutability
t = (1, 2, 3)
t[0] = 5   # not possible

# Methods in Tuple
t.count(1) # Returns the number of times a specified value occurs in a tuple
t.index(2) # Searches the tuple for a specified value and returns the position of where it was found

# Tuple is safe for Constants