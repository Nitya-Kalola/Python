# time - Used for handling time-related operations like delays, timestamps, and time measurements.

import time
time.time() # current time in seconds
# Returns seconds since 1970 (float).
# Used for: generating timestamps, calculating total execution time, logging and retry timeouts

# Example:
start = time.time()
for i in range(0,10):
    print(i)
print(time.time() - start) # Gives time to executes above code.

# time.perf_counter() - Returns a high-resolution time counter that can be used for accurate timing.
# Better than time.time() for performance measuring.
start = time.perf_counter()
for i in range(0,10):
    print(i)
end = time.perf_counter()
print(end - start)

# time.localtime() - Returns a time structure that represents the current local time.
print(time.localtime())

# time.asctime() - Returns a string that represents the current local time in a readable format.
print(time.asctime())

print(time.ctime()) # current day, date and time in string
# time.asctime() converts a time tuple to readable string, while time.ctime() converts seconds since epoch to readable string.

print(time.sleep(10)) # pause the execution of the current thread for a specified number of seconds.
# Use only when: we're intentionally delaying and no event-based wait available

print(time.sleep(0.2)) # 200ms - time.sleep() with float seconds

# Formatting Time
# time.strftime() - Returns a string that represents the current local time in a specified format.
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# Convert human time to epoch
print(time.mktime(time.localtime()))

# time.monotonic() - It ONLY goes forward, never backward (immune to system time changes).
print(time.monotonic()) # Better to use instead of time.time() for timeouts.
