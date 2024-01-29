def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else :
        return m + multiply(m, n-1)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def check(x):
        if x==1:
            return True
        elif n%x==0:
            return False
        else :
            return check(x-1)
    return check(n-1)
    """
    官方答案如下：
    def helper(i):
        if i > (n ** 0.5):      # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)
    """


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
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
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n==1:
        return 1
    elif n%2==0:
        return 1 + hailstone(n//2)
    else :
        return 1 + hailstone(n*3+1)


def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1==0 or n2==0:
        return n1 + n2      #当n1和n2有其中之一为零时，直接返回不为零的那一个，即n1+n2
    elif n1%10 < n2%10:
        return merge(n1//10, n2)*10 + n1%10
    else :
        return merge(n1, n2//10)*10 + n2%10