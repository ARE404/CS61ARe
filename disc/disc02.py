def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    def F(cond):
        for i in range(1,n+1,1):
            if cond(i):
                print(i)
        return F

def curry2(g):
    def f1(x):
        def f2(y):
            return g(x,y)
        return f2
    return f1

def curry2_lambda(g):
    return lambda x:lambda y: g(x,y)

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond>
    and prints out all integers 1..i..n where calling cond(i)
    returns True. The returned function returns another function
    with the exact same behavior.

    >>> def multiple_of_4(x):
    ...     return x % 4 == 0
    >>> def ends_with_1(x):
    ...     return x % 10 == 1
    >>> k = make_keeper_redux(11)(multiple_of_4)
    4
    8
    >>> k = k(ends_with_1)
    1
    11
    >>> k
    <function do_keep>
    """
    # Paste your code for make_keeper here!
    def do_keep(cond):
        for i in range(1,n+1,1):
            if cond(i):
                print(i)
        return make_keeper_redux(n)
    return do_keep

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n<=0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    # ____________________________
    #     ____________________________
    #     while ____________________________:
    #         if ____________________________:
    #             return ____________________________
    #         ____________________________
    #     ____________________________
    # ____________________________

    def F(n):
        # r=n%10
        while n>0:
            if n%pow(10,k)!=n and n//pow(10,k)%10!=n%10:
                return False
            n=n//10
        return True
    return F    

def three_memory(n):
    """
    >>> f = three_memory('first')
    >>> f = f('first')
    Not found
    >>> f = f('second')
    Not found
    >>> f = f('third')
    Not found
    >>> f = f('second') # 'second' was not input three calls ago
    Not found
    >>> f = f('second') # 'second' was input three calls ago
    Found
    >>> f = f('third') # 'third' was input three calls ago
    Found
    >>> f = f('third') # 'third' was not input three calls ago
    Not found
    """
    def f(x, y, z):
        def g(i):
            if ____________________________:
                ____________________________
            else:
                ____________________________
            return ____________________________
        return g(i)
    return f(None, None, n)