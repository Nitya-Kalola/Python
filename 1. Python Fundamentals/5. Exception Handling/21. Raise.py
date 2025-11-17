# Raise - manually triggers an exception.
# Once raised: code stops immediately and control jumps to the nearest except block.

# Syntax: raise Exception("Something went wrong")

# Raising Built-in Exceptions
raise ValueError("Invalid input")
raise TypeError("Expected a string")
raise TimeoutError("Operation took too long")
# We should always raise the MOST SPECIFIC exception possible.
raise Exception("Error") # Not like this

# Raising Custom Exceptions
# We can create our own exceptions:
class LoginError(Exception):
    pass
# and use it as:
raise LoginError("Invalid username or password")

# Using raise Inside try/except
# Raise a new exception inside except
try:
    x = int("abc")
except ValueError:
    raise Exception("Failed to convert string to number") # Called as Exception Translation

# Re-raise the same exception
def calculate_percentage(value, total):
    try:
        return (value / total) * 100
    except ZeroDivisionError:
        print("Error: Total cannot be zero in percentage calculation")
        raise  # Re-raise the same ZeroDivisionError

# Usage
try:
    result = calculate_percentage(50, 0)
except ZeroDivisionError as e:
    print(f"Caught in main: {e}")
# raise without arguments is equal to re-raise original exception.

# Raise inside loops
for user in users:
    if "id" not in user:
        raise KeyError("User missing id")


# Raise inside loops
for user in users:
    if "id" not in user:
        raise KeyError("User missing id")
