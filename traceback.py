import traceback

def foo():
    bar()

def bar():
    baz()

def baz():
    traceback.print_stack()

foo()
