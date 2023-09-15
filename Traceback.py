import traceback

def foo():
    print("Inside foo")
    traceback.print_stack()

def bar():
    print("Inside bar")
    foo()

bar()


# Inside bar
# Inside foo
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/ManuallyPrintStackTrace.py", line 11, in <module>
#     bar()
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/ManuallyPrintStackTrace.py", line 9, in bar
#     foo()
#   File "/Users/yaserrahmani/Desktop/RA-work/pythonCSTG/ManuallyPrintStackTrace.py", line 5, in foo
#     traceback.print_stack()