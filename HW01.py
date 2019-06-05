from operator import add, sub

#Q1: A Plus Abs B
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
a_plus_abs_b(1, -3)

#Q2: Two of Three
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return add(max(a, b, c) * max(a, b, c), ) 
    
#Q3: Largest Factor
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    factors = [k for k in range(1, n) if n % k == 0]
    return max(factors)
    # Iterating from n-1 to 1, we return the first integer that evenly divides n. 
    # This is guaranteed to be the largest factor of n.
    # factor = n - 1
    # while factor > 0:
    #     if n % factor == 0:
    #         return factor
    #     factor -= 1

#Q4: If Function vs Statement
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

#Despite the doctests above, this function actually does not do the same 
#thing as an if statement in all cases. To prove this fact, write functions
#c, t, and f such that with_if_statement returns the number 1, but 
#with_if_function does not (it can do anything else):

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t() # Only go into suite of if statement when c() is True
    else:
        return f() # Only go into else when all if/elif conditions are False

def with_if_function(): # This function needs to do anything else
    return if_function(c(), t(), f()) # THis is  a FUNCTION call

"""
Two steps to evaluating a call expression:
1. Evaluate the operator, then operands(left to right)
2. Apply operator to operands(going into the function)
with_if_function ALWAYS evaluates c(), t(), f() <- f() is not evaluated in with_if_statement
with_if_statement depends on c(). c() = True, then t(), c() = False, then f()
"""

def c():
    return False

def t():
    
    return 1

def f():
    return 1 / 0
    
    
#Q5: Hailstone
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print (n)
    while n != 1:       
        if n % 2 == 0:
            n = n // 2
            print (n)
        elif n % 2 != 0:
            n = n * 3 + 1
            print (n)

hailstone(10)

    #Alternative answer
    # length = 1
    #     while n != 1:
    #         print(n)
    #         if n % 2 == 0:
    #             n = n // 2      # Integer division prevents "1.0" output
    #         else:
    #             n = 3 * n + 1
    #         length = length + 1
    #     print(n)                # n is now 1
    # return length






