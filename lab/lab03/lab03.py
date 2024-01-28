from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    while x>=10 :
        if x%10 < x//10%10 :
            return False
        x //= 10
    return True


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i <= k:
        while n%10 > n//10%10 and n//10>0:
            n //= 10
        final = n % 10
        i = i + 1
        n = n // 10
    return final


def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    smaller = bigger = 0
    if x==1 :
        power_of_two = 1.0
    elif x>1 :
        bigger = 1
        while x>2**bigger:
            smaller, bigger = smaller+1, bigger+1
        if abs(x-2**bigger)<=abs(x-2**smaller):
            power_of_two = 1.0*2**bigger
        else :
            power_of_two = 1.0*2**smaller
    else :
        smaller = -1
        while x<2**smaller:
            smaller, bigger = smaller-1, bigger-1
        if abs(x-2**bigger)<=abs(x-2**smaller):
            power_of_two = 1.0*2**bigger
        else :
            power_of_two = 1.0*2**smaller
    return power_of_two


def make_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def repeat(x):
        i = n
        k = identity
        while i>0:
            k = composer(func,k)
            i -= 1
        return k(x)
    return repeat

def composer(func1, func2):
    """Returns a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f

def apply_twice(func):
    """Returns a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    return make_repeater(func, 2)


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = 2
    while i<=n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x%i==0 or f(x))(checker, i)
        i = i + 1
    return checker
    '''
    此题较难,题干中的any意为任意而非任何
    因此只要参数x可以被在2到n之间的任意一个数字整除,返回值就他应该为True
    此题可采用递归(归纳)的思想,判断i时 x%i==0 or checker(x) (x为参数)是否成立
    再将这一式子的结果赋值给checker函数,这样只要有一个数可以整除x,结果均为True,否则为False
    '''

def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = 2
    while i<=n:
        if not checker(i):
            def outer(f,i):
                def inner(x):
                    return x%i==0 or f(x)
                return inner
            checker = outer(checker,i)
        i = i + 1
    return checker

