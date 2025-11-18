# SYS - Sys gives us direct access to the Python interpreter internals like CLI arguments, exit control, module search paths, runtime info and stdin/stdout/stderr streams.

# sys.argv - It is a list of command line arguments passed to the script.
import sys

print("All arguments:", sys.argv)
print("Number of arguments:", len(sys.argv))

if len(sys.argv) > 1:
    print("You provided these arguments:", sys.argv[1:])
else:
    print("No arguments provided")

# Run above code using below given command in Terminal:
# Note: Change the path to the current directory

# Basic run
# python "25. SYS Module.py"

# With arguments
# python "25. SYS Module.py" hello world 123

# With filename
# python "25. SYS Module.py" myfile.txt

# sys.exit() - Stops your Python program immediately.
sys.exit(0) # Here 0 represents successful exit without any error, if it is non-zero, it will be considered as an error.

print("Hello, World!") # This will not run

# Execute this command in Terminal: python "25. SYS Module.py"

# Exit with message
sys.exit("Critical failure: invalid config")

# sys.stdout - It is a reference to the standard output stream.
sys.stdout.write("Running...\n") # Output : Running...11

# sys.stderr - It is a reference to the standard error stream.
sys.stderr.write("ERROR: Something failed\n") # Output : ERROR: Something failed24

# sys.path - It is a list of directories where Python looks for modules.
print(sys.path) 

# We can add custom folders to where Python looks for modules.
sys.path.append("path/to/folder")

# sys.version - It gives us the version of Python we are currently using.
print(sys.version)

# sys.platform - It gives us the name of the current platform(Windows, Linux, etc).
print(sys.platform)

# sys.modules - It is a dictionary that contains all the currently loaded modules.
print(sys.modules)

# sys.getsizeof() - It returns the size of an object in bytes (Memory Usage).
print(sys.getsizeof(10))

# sys.stdin - It is a reference to the standard input stream.
print(sys.stdin.read())

# sys.getrefcount() - It returns the number of references to an object.
print(sys.getrefcount(10))
