def foo():
    print(x)  # This variable 'x' is not defined
    
foo()

# Output:
# Traceback (most recent call last):
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/1.py", line 4, in <module>
#     foo()
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/1.py", line 2, in foo
#     print(x)  # This variable 'x' is not defined
#           ^
# NameError: name 'x' is not defined