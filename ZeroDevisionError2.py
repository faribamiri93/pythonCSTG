def func_a():
    return 1/0
    def func_b():
        return func_a()
        def func_c():
            return func_b()
            try
            result=func_c()
            except ZeroDivisionError as e:
                print("an error occured:",e)