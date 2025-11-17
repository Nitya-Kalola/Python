# List - ordered, mutable, indexable, dynamic (grows/shrinks), heterogeneous (can store mixed data types)
# Internally, it’s a dynamic array of pointers to objects (stores references, not actual values).

# Creating List
nums = [1, 2, 3]
mixed = [1, "a", True, 3.14]
empty = []

# Using constructor:
lst = list()

# Indexing
nums[0]
nums[-1]
nums[-2]

# Slicing
lst[1:4]      # elements 1,2,3
lst[:3]       # first 3
lst[2:]       # from index 2 to end
lst[::-1]     # reverse
# Slicing creates a new list, not a reference to the original.

# Mutability - means operations modify the ORIGINAL list.

a = [1,2,3]
b = a # Both reference the same list object.
b.append(4)

print(a)   # Output : [1,2,3,4]

# List Methods

# 1) append() - Adds one element at the end.
a.append(10)

# 2) extend() - Adds multiple elements.
a.extend([20, 30])

# 3) insert() - Insert at specific index.
a.insert(1, 99)

# 4) pop() - Removes & returns element.
x = a.pop()       # last
y = a.pop(2)      # index 2

# 5) remove() - Removes FIRST occurrence.
a.remove(5)

# 6) clear() - removes all elements from a list, making it empty.
a.clear()

# 7) index() - finds the first occurrence of a specified element and returns its zero-based index.
a.index("a")

# 8) count() - count the number of times a specific element appears in a list.
a.count(10)

# 9) sort() - sort original list.
a.sort()
a.sort(reverse = True) # sort elements of list in Descending Order
words = ["Banana", "apple", "Cherry"]
words.sort(key=str.lower) # Sorting a list of strings case-insensitively

# 10) sorted() - Returns new sorted list.
b = sorted(a)

# List Comprehension
new = [x * 2 for x in nums]


# Nested List (Matrix):
matrix = [
    [1,2,3],
    [4,5,6],
]

# Accessing element
matrix[0][1] # Output : 2

# Copying a Lists:
# Shallow copy
b = a.copy()
b = list(a)
b = a[:]
# Deep Copy
import copy
b = copy.deepcopy(a)

# Repetition
[0] * 5   # Output:  [0,0,0,0,0]

# Membership
# if 10 in lst:
# Checks if 10 is inside the lst or not.


# Avoid this mistakes:
"""
- Using list inside function default
def f(x=[]):

- Confusing append() vs extend()
- Sorting mixed data types (Python 3 forbids it)
- Forgetting copy() and modifying shared list accidentally
- Using list multiplication incorrectly with nested lists
- Using list for queue/stack operations instead of deque
"""