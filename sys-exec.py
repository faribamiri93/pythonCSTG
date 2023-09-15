import sys

def function_with_exception():
    x = 1 / 0

try:
    function_with_exception()
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback)


# Traceback (most recent call last):
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/sys-exec.py", line 8, in <module>
#     function_with_exception()
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/sys-exec.py", line 5, in function_with_exception
#     x = 1 / 0
#         ~~^~~
# ZeroDivisionError: division by zero