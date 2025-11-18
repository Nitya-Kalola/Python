# OS - It provides functions for interacting with the operating system like file handling, directory navigation, environment variables, process info, path operations and system commands

import os
print(os.getcwd()) # Gives Current Working Directory

os.chdir("path/to/dir") # Changing Directory
# Note : Use \\ in path instead of \ to avoid an errors.

os.listdir("path/to/dir") # List all files in a directory

os.listdir(".") # "." represents the current working directory.

os.path.exists("path/to/dir") # Returns True if given path of directory or any file is exists otherwise False.

os.path.isfile("path/to/file") # Returns True if the given path is for an existing file only; otherwise (if a directory), it is False.

os.path.isdir("path/to/dir") # Returns True if the given path is for an existing directory only; otherwise (if a file), it is False.

os.mkdir("path/to/dir") # Creates a directory.

os.rmdir("path/to/dir") # Removes empty folder.

os.makedirs("path/to/dir") # Creates nested folders.

os.remove("path/to/file") # Removes a file.

os.removedirs("path/to/dir") # Removes nested folders.

import shutil
shutil.rmtree("path/to/dir") # Removes a directory tree with the available contents in it.
# Can be dangerous

# Environment Variables - A dynamic named value stored by the operating system that can affect how running processes behave on a computer.
os.getenv("VARIABLE_NAME") # Returns value of the variable if exists otherwise None

os.environ["VARIABLE_NAME"] = "VALUE" # sets an environment variable with its value.

# Joining Paths

# BAD - Platform dependent
windows_bad = "folder\\subfolder\\file.txt"    # Windows
unix_bad = "folder/subfolder/file.txt"         # Mac/Linux


# GOOD - Platform Independent
path_good = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined path: {path_good}")
# Output on Windows: folder\subfolder\file.txt
# Output on Mac/Linux: folder/subfolder/file.txt

# Useful Path Operations

path = "/home/user/documents/report.pdf"

# Get filename
print(os.path.basename(path))      # Output: "report.pdf"

# Get directory
print(os.path.dirname(path))       # Output: "/home/user/documents"

# Get full absolute path  
print(os.path.abspath("file.txt")) # Output: "/current/folder/file.txt"

# Split filename and extension
print(os.path.splitext(path))      # Output: ("/home/user/documents/report", ".pdf")

# Shows us what files/folders are in the current directory
os.system("dir")

# Returns the size of the file in bytes
os.path.getsize("path/to/dir")

# Returns a stat_result object
os.stat("path/to/dir")
