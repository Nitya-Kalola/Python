# import - Used to loading a module object into memory ONCE, and then referencing it.

# Module - Collection of Classes, Functions and Methods. In general a simple.py file.
# Package - Collection of Multiple Modules.
# Library - Collection of Packages.

# Example:
import math # This loads the math module and binds it to the name math.

# Using math module:
print(math.sqrt(16))

"""
Use "import module" when:

- we want clarity
- we need many functions from the same module
- we want to avoid namespace pollution
"""

# from import
from math import sqrt # This imports ONLY the name sqrt into our namespace.
print(sqrt(16)) # No need for qualifying with math.

"""
Use "from module import X" when:

- we only need a specific function
- we want shorter names
- readability improves
"""

# Never do this: from math import *
# Do this instead only: import math

# Importing With Aliases (as) - Used to keep the Short name temporary for the Module
from math import sqrt as sq
print(sq(16))

# For conflicting names:
# from module_a import config as config_a
# from module_b import config as config_b

# Note : Imports Are Executed Only Once, Subsequent imports reference same loaded module.
# Example:
import math
import math # references same module

# Module-level code: execute top-level code first. 
# Bad Module:

# dangerous_module.py Code:
print("Connecting to the company database...") # Logs a confusing message as soon as it's imported.
connection = connect_to_database() # Tries to connect for real! Even if the main program doesn't need it.

print("Launching a web browser...")
browser = selenium.start_browser() # Pops open a browser window on your screen!

print("Doing a calculation...")
result = 10 / 0 # This will crash the ENTIRE program on import!

"""
When we import dangerous_module, our program will immediately:

- Print confusing messages.
- Try to connect to a database it might not need.
- Open a blank browser window on your screen.
- CRASH with a "division by zero" error before it even does anything useful!
"""

# Good Module:
# clean_module.py Code:

x = 10

def get_database_connection():
    print("Connecting to database now...")
    connection = connect_to_database()
    return connection

def start_web_browser():
    print("Starting browser now...")
    browser = selenium.start_browser()
    return browser

# Main Program: main.py

import clean_module

print(clean_module.x)
connection = clean_module.get_database_connection()
browser = clean_module.start_web_browser()
# The program is in control.
# This is a better way to import modules.

# Importing From Sub-folders (Packages)

# Folder:
"""
framework/
    __init__.py
    pages/
        __init__.py
        login.py
"""
# Use: from framework.pages.login import LoginPage
# __init__.py makes the folder a package (Python searches it).

# Circular Imports:
# File A: from B import funcB
# File B: from A import funcA
# This will crash.

# Solution: restructure, move logic to a shared module or import inside functions instead of at top

# Absolute vs Relative Imports:
# Absolute(Recommended): from framework.pages.login import LoginPage
# Relative(for packages): from .login import LoginPage or use (..) instead of (.) to access the parent folder. We can also use (...) to access the grandparent folder.

# Note: Never import inside loop, because it will import the same module multiple times.
