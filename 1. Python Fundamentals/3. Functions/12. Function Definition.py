# Function - A function is a reusable block of code that: takes input (optional), processes logic and returns output (optional).
# We can store it into variables, pass it to other functions and return it.
# It is an Object.

# Syntax:
"""
def function_name(parameters):
    # body
    return value
"""

# Example:
def add(a, b):
    """Return the sum of a and b.""" # Defining docstring is Good in Functions.
    return a + b

output = add(4,5)
print(output)

# Note: A function without a return statement returns None by default.

# A good function name MUST be descriptive, be lowercase_with_underscores and reflect EXACT action.

"""
Examples (good):

click_button()
get_user_data()
parse_json()
"""

"""
Bad examples:

fun()
test1()
abc()
"""
