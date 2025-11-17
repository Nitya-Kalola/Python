# Default Arguments - gives a parameter a value if no argument is provided.

def func(a, b=10):
    return a + b

func(5)        # b uses default = 10, output 15
func(5, 20)    # b = 20, output 25

# Rule : Default arguments are evaluated ONCE at function definition time — not every call.

# Default Arguments With Keyword Arguments:
def greet(name, msg="Hello"):
    print(msg, name)

greet("Nitya")                # Hello Nitya
greet("Nitya", msg="Hi")      # Hi Nitya

# Function Metadata Stored with Defaults
def f(a, b=5, c=10):
    pass

print(f.__defaults__)   # Output: (5, 10)

