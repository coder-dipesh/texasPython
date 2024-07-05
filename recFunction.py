# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)





# Factorial

def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)
'''
factorial(5)
  -> 5 * factorial(4)
    -> 4 * factorial(3)
      -> 3 * factorial(2)
        -> 2 * factorial(1)
          -> 1 (base case)
        -> 2 * 1 = 2
      -> 3 * 2 = 6
    -> 4 * 6 = 24
  -> 5 * 24 = 120

'''

#  Testing the function
print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
print(factorial(0))  # Output: 1