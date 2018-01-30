def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    # if b == 0:
    #     return c
    return a + ab_plus_c(a, b-1,c)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    # 答案
    # a, b = max(a, b), min(a, b) 注意a和b的大小
    # if a % b == 0:
    #     return b
    # else:
    #     return gcd(b, a % b)
    # Iterative solution, if you're curious
# def gcd_iter(a, b):
#     """Returns the greatest common divisor of a and b, using iteration.

#     >>> gcd_iter(34, 19)
#     1
#     >>> gcd_iter(39, 91)
#     13
#     >>> gcd_iter(20, 30)
#     10
#     >>> gcd_iter(40, 40)
#     40
#     """
#     if a < b:
#         return gcd_iter(b, a)
#     while a > b and not a % b == 0:
#         a, b = b, a % b
#     return b

# print(gcd(40, 40))


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return(hailstone(n//2))
        else:
            return(hailstone(n*3+1))

    # 答案1
    # print(n)
    # if n == 1:
    #     return 1
    # elif n % 2 == 0:
    #     return 1 + hailstone(n // 2)
    # else:
    #     return 1 + hailstone(3 * n + 1)

    #答案2
# Alternate solution with helper function
# def hailstone2(n):
#     def hail_helper(n, count):
#     print(n)
#     if n == 1:
#         return count
#     else:
#         if n % 2 == 0:
#         return hail_helper(n // 2, count + 1)
#         else:
#         return hail_helper(3 * n + 1, count + 1)
#     return hail_helper(n, 1)


# print(hailstone(10)) 
