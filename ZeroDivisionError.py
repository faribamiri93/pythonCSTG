def divide(a, b):
    return a / b  # Division by zero will raise an exception

try:
    result = divide(10, 0)  # This will raise a ZeroDivisionError
except Exception as e:
    import traceback
    traceback.print_exc()

# output:
# Traceback (most recent call last):
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/ZeroDivisionError.py", line 5, in <module>
#     result = divide(10, 0)  # This will raise a ZeroDivisionError
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/ZeroDivisionError.py", line 2, in divide
#     return a / b  # Division by zero will raise an exception
# ZeroDivisionError: division by zero