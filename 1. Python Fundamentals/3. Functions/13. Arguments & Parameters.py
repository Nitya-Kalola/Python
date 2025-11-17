# Parameters - Names listed in the function definition.

def add(a, b):   # a, b are PARAMETERS
    return a + b

# Arguments - Actual values you pass when calling the function.

add(5, 10)       # 5, 10 are ARGUMENTS

# Types of Parameters:

# 1) Positional Parameters: Order MATTERS.

def greet(name, age):
    print(name, age)

greet("Nitya", 20)          # correct
greet(20, "Nitya")          # wrong order -> wrong meaning

# 2) Keyword Parameters: Order DOESN’T matter.

def greet(name, age):
    print(name, age)

greet(age=20, name="Nitya")

# Note: Don’t mix positional after keyword
# Example: greet(age=20, "Nitya")

# Default Parameter

def greet(name, age = 20): # age is default to 20
    print(name, age)

greet("Nitya") # Normal Call
greet("Nitya", 20) # Override

# Mutable Defaults:

def f(items=[]):   # BAD
    items.append(1)
    return items

print(f())  # [1]
print(f())  # [1, 1]
print(f())  # [1, 1, 1]

# This happens because:
"""
1) Default arguments are evaluated ONLY ONCE when the function is defined
2) The same [] list object is reused for every function call
3) All calls share the same mutable list in memory
"""

# Correct:
def f(items=None):
    if items is None:
        items = []

# *args — Variable Positional Arguments : Used when we don’t know how many arguments we'll receive.

def add(*nums): # *nums becomes a tuple.
    return sum(nums)

add(1, 2, 3, 4)

# **kwargs — Variable Keyword Arguments : Used for flexible named arguments.

def info(**data): # **data becomes a dict.
    print(data)

info(name="Nitya", age=20)

# Combined Parameters:

"""
Order We MUST Follow:

1) Positional parameters
2) Default Parameters
3) *args (Variable Positional Arguments)
4) Keyword parameters
5) **kwargs (Variable Keyword Arguments)
"""

def test(a, b, *args, x=10, y=20, **kwargs):
    pass

# Argument Unpacking

# Passing a list into *args:
nums = [1,2,3]
add(*nums)


# Passing a dict into **kwargs:
config = {"timeout": 10, "verify": False}
add(**config)


# Pass-by-Assignment: Python doesn't pass by value or reference. It passes object references.

def modify(lst):
    lst.append(4) # Here list got appended, Because list is mutable.

nums = [1,2,3]
modify(nums)
print(nums)  #Output: [1,2,3,4]
