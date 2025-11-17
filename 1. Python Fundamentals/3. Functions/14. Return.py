# Return - immediately stops the function and gives a value back to the caller.

# Syntax: return value

# Returning Value:
def add(a, b):
    return a + b

# No return:

def hello():
    print("Hi")
# hello() implicitly returns None.

# It may generate confusion: Using the return value of a function that returns None:
x = print("hello")
print(x)   # None

# Returning Multiple Values:

def stats():
    return 10, 20, 30 # It returns a tuple of (10,20,30)

a, b, c = stats()

# Bad:
def info():
    return 1, "success", [1,2]

# Better:
def info():
    return {
        "code": 1,
        "msg": "success",
        "data": [1,2]
    }

# Early Return — Clean Alternative to Deep Nesting

# Bad Code:
def validate(user):
    if user:
        if "id" in user:
            if user["id"] > 0:
                return True
    return False

# Good Code:
def validate(user):
    if not user:
        return False
    if "id" not in user:
        return False
    if user["id"] <= 0:
        return False
    return True
# Early return = less nesting = cleaner logic.

# Returning From Loops:
def find_user(users, target):
    for user in users:
        if user["id"] == target:
            return user
    return None

# Returning from Try/Except:
def safe_div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

# Returning Functions (Higher-Order Functions)
# Functions are objects — we can return them.

def outer():
    def inner():
        return "Hello"
    return inner

fn = outer()
print(fn())

# Returning Nothing but Still Using Return
def log():
    print("done")
    return
# We can explicitly return without value.
