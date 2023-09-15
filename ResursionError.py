def recursive_function(n):
    if n <= 0:
        return
    recursive_function(n + 1)

try:
    recursive_function(1)
except RecursionError as e:
    print(f"Recursion error occurred: {e}")


# output:
# Recursion error occurred: maximum recursion depth exceeded