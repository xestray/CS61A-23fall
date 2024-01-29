def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp<60 or raining


def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    if n%10<5:
        return n - n % 10
    else :
        return n - n % 10 +10


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    i = 1
    while i<=n:
        if i%15==0:
            print('fizzbuzz')
        elif i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        else :
            print(i)
        i += 1


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n==1:
        return False
    k = 2
    while k<n:
        if n%k==0:
            return False
        k += 1
    return True


def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>>  # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    cnt = i =0
    while i<=9:
        if has_digit(n, i):
            cnt += 1
        i += 1
    return cnt

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    while n>0:
        if n%10==k:
            return True
        n //= 10
    return False
