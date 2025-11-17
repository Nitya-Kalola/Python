# Set - unordered, mutable, unique elements only, hash-based (fast lookups)
# Internally, it’s implemented as a hash table.

# Creating Set
# Basic set:
s = {1, 2, 3}

# Using set() constructor:
s = set([1, 2, 3])

# Empty set:
s = set()
s = {} # This is Dictionary, not a set



# We cannot store: lists, dicts, other sets. But we can store tuples (if elements inside are also hashable).

# Basic Set Operations:
# Add element
s.add(10)

# Remove element (throws error if missing)
s.remove(10)

# Discard element (safe)
s.discard(10)

# Pop random element
s.pop()

# Clear set
s.clear()

# Mathematical Set Operations (Super Useful)
s1 = {1,2,3}
s2 = {3,4,6}

# Union (combine)
s1 | s2
s1.union(s2)

# Intersection (common elements)
s1 & s2
s1.intersection(s2)

# Difference (in s1 but not s2)
s1 - s2
s1.difference(s2)

# Symmetric Difference (exclusive)
s1 ^ s2
s1.symmetric_difference(s2) # Gives output of elements that are unique in both sets.

# Set Comprehension : {x*x for x in range(10)}

# Frozen set - immutable set.
fs = frozenset([1,2,3])
